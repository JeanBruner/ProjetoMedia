from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.notas, name='notas'),
    path('', TemplateView.as_view(template_name='list.html'), name='home'),
    path('admin/', admin.site.urls)
]
