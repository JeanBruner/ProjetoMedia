from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='media/login.html',
        ),
        name="login"
    ),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('', RedirectView.as_view(url=reverse_lazy('mostrar'))),
    path('admin/', admin.site.urls),
    path('alunos/', views.Notas.as_view(), name="mostrar")
]
