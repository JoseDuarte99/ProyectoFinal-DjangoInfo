
from django.http import JsonResponse
from .forms import RegForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views import View
from django.contrib.auth import logout

# Create your views here.

class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = RegForm
    success_url = reverse_lazy('apps.user:login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        return super().form_valid(form)

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('index')

class LogoutUsuario(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('index')

class UserProfile(LoginRequiredMixin, TemplateView):
        template_name = 'user_profile.html'