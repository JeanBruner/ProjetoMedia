from django import forms
from media.models import Aluno
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CadForm(ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'aluno',
            'nota1',
            'nota2',
            'nota3',
        ]
