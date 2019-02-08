from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import Aluno
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import CadForm
from django.views.generic import ListView
from django.views.generic import CreateView


class Notas(ListView):
    model = Aluno
    template_name = "media/list.html"


class Cadastro(CreateView):
    template_name = 'media/cad.html'
    model = Aluno
    form_class = CadForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('cadastro'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'media/login.html', {'form': form})
