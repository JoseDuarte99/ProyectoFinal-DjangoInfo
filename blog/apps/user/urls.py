from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'apps.user'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutUsuario.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', UserProfile.as_view(), name='user_profile'),

    path('manage-users/', UserListView.as_view(), name='manage_users'),
    path('edit-user/<int:pk>/', UserUpdateView.as_view(), name='edit_user'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
    
]