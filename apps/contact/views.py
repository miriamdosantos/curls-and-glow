from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from apps.users.models import UserProfile

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_message = contact_form.save(commit=False)
            
            if request.user.is_authenticated:
                try:
                    # Obtém o UserProfile associado ao usuário autenticado
                    user_profile = UserProfile.objects.get(user=request.user)
                    contact_message.user_profile = user_profile
                except UserProfile.DoesNotExist:
                    # Se UserProfile não existir, não atribua nada e continue
                    contact_message.user_profile = None
            else:
                contact_message.user_profile = None

            contact_message.save()
            messages.success(request, 'Contact message received. I endeavor to respond within 2 working days')
            return redirect('contact')  # Redireciona para a URL nomeada 'contact'
    else:
        contact_form = ContactForm()  # Inicializa o formulário para GET

    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact/contact.html', context)
