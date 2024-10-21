from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _



class ContactAnonymousForm (forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']
        labels = {
            'full_name': _('Nombre y Apellido'),
            'email': _('Correo Electrónico'),
            'subject': _('Asunto'),
            'message': _('Mensaje'),
        }

class ContactAuthenticatedForm (forms.ModelForm):
    full_name = forms.CharField(disabled=True, label=_('Nombre y Apellido'))
    email = forms.EmailField(disabled=True, label=_('Correo Electrónico'))

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']
        labels = {
            'subject': _('Asunto'),
            'message': _('Mensaje'),
        }