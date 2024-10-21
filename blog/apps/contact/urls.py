from django.urls import path
from . import views

app_name = 'apps.contact'

urlpatterns = [
    path("", views.ContactUsuer.as_view(), name='contact'),
    path("success", views.ContactSuccess.as_view(), name='contact_success'),
]