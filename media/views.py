from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import Aluno
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import CadForm
from django.contrib.auth.decorators import user_passes_test


def notas(request):
    suppliers = Aluno.objects.all()
    context = {
       'supplier_list': suppliers
    }
    return render(request, 'media/list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def cadastro(request):
    if request.method == 'POST':
        form = CadForm(request.POST)
        if form.is_valid():
            form.save()
            form = CadForm()
    else:
        form = CadForm()
    return render(request, 'media/cad.html', {'cadform': form})


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
