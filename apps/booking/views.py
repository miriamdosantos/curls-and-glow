from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from apps.services.models import Service
from apps.stylists.models import Stylist, Availability
from apps.users.models import UserProfile
from .models import Booking, Offer

# Função auxiliar para encapsular a lógica de encontrar horários livres
def get_free_slots(selected_date_obj, available_slots, booked_slots, duration_if_booked=timedelta(hours=2), interval_if_free=timedelta(minutes=30)):
    free_slots = []
    
    for availability in available_slots:
        current_time = datetime.combine(selected_date_obj, availability.start_time)
        end_time = datetime.combine(selected_date_obj, availability.end_time)

        # Calcula o último horário disponível (uma hora antes do horário final)
        last_booking_time = end_time - timedelta(hours=1)

        while current_time < end_time:
            # Verifica se o horário está reservado
            is_booked = booked_slots.filter(date_time__time=current_time.time()).exists()

            # Verifica se o horário atual está disponível e é válido (antes do último horário de agendamento)
            if not is_booked and current_time <= last_booking_time:
                free_slots.append(current_time.time())  # Adiciona o horário se não estiver reservado

            # Se o horário estiver reservado, pular para o próximo horário disponível em 2 horas
            if is_booked:
                current_time += duration_if_booked
            else:
                # Caso contrário, incrementar em 30 minutos
                current_time += interval_if_free

    return free_slots


# View para agendar o atendimento
def make_appointment(request):
    stylists = Stylist.objects.all()
    context = {'stylists': stylists}
    return render(request, 'booking/booking.html', context)

# View para selecionar a data e horários disponíveis
def select_date(request):
    services = Service.objects.all()
    
    if request.method == "POST":
        selected_stylist_id = request.POST.get("selected_stylist_id")
        selected_date = request.POST.get("date-calendar")

        # Verifique se a data foi recebida corretamente
        if not selected_date:
            messages.error(request, "No date selected. Please select a valid date.")
            return redirect('booking')

        # Tenta converter a string de data em um objeto datetime
        try:
            selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
        except ValueError:
            messages.error(request, "Invalid date format. Please try again.")
            return redirect('booking')

        day_of_week_name = selected_date_obj.strftime('%A')

        # Se o estilista selecionado for uma string vazia, buscar todos os horários disponíveis
        if selected_stylist_id == "":
            available_slots = Availability.objects.filter(day_of_week=day_of_week_name)
            booked_slots = Booking.objects.filter(date_time__date=selected_date_obj)
        else:
            # Se um estilista específico foi selecionado, filtrar horários por ele
            stylist_id = int(selected_stylist_id)
            available_slots = Availability.objects.filter(stylist__id=stylist_id, day_of_week=day_of_week_name)
            booked_slots = Booking.objects.filter(stylish__id=stylist_id, date_time__date=selected_date_obj)

        # Usa a função auxiliar para encontrar horários livres
        free_slots = get_free_slots(selected_date_obj, available_slots, booked_slots)

        # Formatar os horários para exibição
        formatted_slots = [time.strftime("%I:%M %p") for time in free_slots]

        context = {
            'selected_date': selected_date,
            'selected_stylist_id': selected_stylist_id,
            'available_times': formatted_slots,
            'services': services
        }

        return render(request, 'booking/select_time.html', context)

    return redirect('booking')

@login_required
def book_appointment(request):
    if request.method == "POST":
        selected_time = request.POST.get("time")  # Ex: '9:30 AM'
        selected_date = request.POST.get("selected_date")  # Ex: '2024-10-12'
        selected_stylist_id = request.POST.get("selected_stylist_id")
        selected_service_id = request.POST.get("service")
        coupon_code = request.POST.get("coupon")
        if coupon_code:
            coupon_code = coupon_code.strip().upper()
        # Verificar se o stylist e o serviço são válidos
        stylist = get_object_or_404(Stylist, id=selected_stylist_id) if selected_stylist_id else None
        service = get_object_or_404(Service, id=selected_service_id)

        # Ajustar o formato do tempo para lidar com '9:30 AM' corretamente
        try:
            selected_datetime = datetime.strptime(
                f"{selected_date} {selected_time.replace(' a.m.', ' AM').replace(' p.m.', ' PM')}",
                "%Y-%m-%d %I:%M %p"  # Inclui minutos (%M)
            )
        except ValueError:
            messages.error(request, "Invalid date or time format. Please try again.")
            return redirect('select_time')

        # Verificar se o cupom é válido
        offer_instance = None
        if coupon_code:
            
            try:
                offer_instance = Offer.objects.get(code=coupon_code, end_date__gte=timezone.now())
            except Offer.DoesNotExist:

                
                # Recarregar os horários e serviços disponíveis para renderizar novamente na página
                selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
                day_of_week_name = selected_date_obj.strftime('%A')
                
                available_slots = Availability.objects.filter(stylist__id=selected_stylist_id, day_of_week=day_of_week_name)
                booked_slots = Booking.objects.filter(stylish__id=selected_stylist_id, date_time__date=selected_date_obj)
                
                free_slots = get_free_slots(selected_date_obj, available_slots, booked_slots)
                formatted_slots = [time.strftime("%I:%M %p") for time in free_slots]
                services = Service.objects.all()

                return render(request, 'booking/select_time.html', {
                    'show_invalid_coupon_modal': True,
                    'selected_date': selected_date,
                    'selected_stylist_id': selected_stylist_id,
                    'available_times': formatted_slots,
                    'services': services
                })

        # Verificar se o horário já foi reservado
        if Booking.objects.filter(stylish=stylist, date_time=selected_datetime).exists():
            messages.error(request, "This time slot is already booked.")
            return redirect('select_time')

        # Obter o perfil do usuário
        user_profile = get_object_or_404(UserProfile, user=request.user)

        # Criar a reserva
        Booking.objects.create(
            stylish=stylist,
            service=service,
            user_profile=user_profile,
            date_time=selected_datetime,
            offer=offer_instance  # Atribui a oferta se houver
        )

        messages.success(request, "Appointment successfully booked!")
        return redirect('booking')  # Redireciona após o sucesso

    return redirect('booking')  # Caso não seja POST
