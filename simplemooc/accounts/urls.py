from django.urls import path
from django.contrib.auth import views as auth_view
from simplemooc.accounts import views

app_name='accounts'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrar/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', auth_view.LogoutView.as_view(next_page='core:home'), name='logout'),
    path('cadastra-se/', views.register, name='register'),
    path('nova-senha/', views.password_reset, name='password_reset'),
    path('confirmar-nova-senha/<str:key>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),
]
