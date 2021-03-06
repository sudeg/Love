from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


class SignupView(FormView):

    form_class = forms.SignupForm
    template_name = 'authentication/Signup.html'
    success_url = reverse_lazy('authentication:dashboard')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)



def Dashboard(request):
    return render(request, 'authentication/dashboard.html')


def Logout(request):

    logout(request)
    return HttpResponseRedirect(reverse_lazy('authentication:dashboard'))


class LoginView(FormView):

    form_class = forms.LoginForm
    success_url = reverse_lazy('authentication:dashboard')
    template_name = 'authentication/login.html'

    def form_valid(self, form):

        credentials = form.cleaned_data

        user = authenticate(username=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('authentication:login'))