from django.shortcuts import render
from .forms import ContactAnonymousForm, ContactAuthenticatedForm
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class ContactUsuer(CreateView):
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('apps.contact:contact_success')
    form_class = ContactAnonymousForm

    def get_form_class(self):
        if self.request.user.is_authenticated:
            return ContactAuthenticatedForm
        else:
            return ContactAnonymousForm

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['full_name'] = self.request.user.get_full_name()
            initial['email'] = self.request.user.email
        return initial


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Consulta enviada con exito.')
        return super().form_valid(form)

class ContactSuccess(TemplateView):
    template_name = 'contact/contact_success.html'