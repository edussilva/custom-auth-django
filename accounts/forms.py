# coding: utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email']



class UserNonAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name']


class UserProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'cpf',
            'nascimento',
            'telefone1',
            'telefone2',
            'newsletter',
        )

    def __init__(self, *args, **kwargs):
        super(UserProfileCreationForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].required = True
        self.fields['nascimento'].required = True
        self.fields['telefone1'].required = True


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'name', 'is_active', 'is_staff']
