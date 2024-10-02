from django.test import TestCase
from django.urls import reverse
from .models import Service

class ServicesViewsTests(TestCase):
    
    def setUp(self):
        # Criando dados de exemplo para o modelo Service
        Service.objects.create(title="Serviço 1")
        Service.objects.create(title="Serviço 2")

    def test_home_view(self):
        # Testando a visualização da página inicial
        response = self.client.get(reverse('home'))  # Testa a URL 'home'
        self.assertEqual(response.status_code, 200)  # Verifica se o código de status é 200 (OK)
        self.assertTemplateUsed(response, 'services/index.html')  # Verifica se o template usado é 'services/index.html'

    def test_services_view(self):
        # Testando a visualização da página de serviços
        response = self.client.get(reverse('services'))  # Testa a URL 'services'
        self.assertEqual(response.status_code, 200)  # Verifica se o código de status é 200 (OK)
        self.assertTemplateUsed(response, 'services/services.html')  # Verifica se o template usado é 'services/services.html'
        self.assertContains(response, "Serviço 1")  # Verifica se o conteúdo esperado ("Serviço 1") está na resposta
