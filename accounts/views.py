# coding: utf-8

from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
from .models import User
from .forms import UserProfileCreationForm, UserNonAdminCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login


class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserNonAdminCreationForm
    success_url = reverse_lazy('accounts:index')


def register(request):

    if request.method == 'POST':
        form = UserNonAdminCreationForm(request.POST)
        form_profile = UserProfileCreationForm(request.POST)

        if all([form.is_valid(), form_profile.is_valid()]):
            user = form.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            email = request.POST.get('email')
            password = request.POST.get('password1')
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)

            return redirect('home')
    else:
        form = UserNonAdminCreationForm()
        form_profile = UserProfileCreationForm()

    context = {
        'form': form,
        'form_profile': form_profile,
    }

    return render(request, 'accounts/register.html', context)



class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return  kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)

#register = RegisterView.as_view()
index = IndexView.as_view()
#update_user = UpdateUserView.as_view()
#update_password = UpdatePasswordView.as_view()
