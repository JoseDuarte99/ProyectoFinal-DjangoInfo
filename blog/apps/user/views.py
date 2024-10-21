from .forms import RegForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View 
from django.contrib.auth import logout
from django.views.generic import ListView, UpdateView, DeleteView
from .models import User
from .forms import UserAdministrationForm
from django.core.exceptions import PermissionDenied

# Create your views here.

class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


#  --------------------------------------- REGISTRO ------------------------------------------------

# REGISTRO DE USUARIO
class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = RegForm
    success_url = reverse_lazy('apps.user:login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        return super().form_valid(form)



#  --------------------------------------- LOGIN Y LOGOUT ------------------------------------------------

# INICIO DE SESION
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('index')

# CIERRE DE SESION
class LogoutUsuario(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('index')



#  --------------------------------------- PERFIL ------------------------------------------------

# PERFIL DEL USUARIO
class UserProfile(LoginRequiredMixin, TemplateView):
        template_name = 'user/user_profile.html'



#  --------------------------------------- USER ------------------------------------------------

# LISTA DE USUARIOS
class UserListView(ListView):
    model = User
    template_name = 'user/manage_users.html'
    context_object_name = 'users'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or (request.user.username != 'Administrador' and request.user.username != 'SuperUser'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# EDITAR USUARIOS
class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdministrationForm
    template_name = 'user/edit_user.html'
    success_url = reverse_lazy('apps.user:manage_users')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or (request.user.username != 'Administrador' and request.user.username != 'SuperUser'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# ELIMINAR USUARIOS
class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/confirm_delete_user.html'
    success_url = reverse_lazy('apps.user:manage_users')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or (request.user.username != 'Administrador' and request.user.username != 'SuperUser'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)