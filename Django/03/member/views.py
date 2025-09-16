from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from mysite import settings
from django.contrib.auth import login as django_login
from django.urls import reverse
def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)
    context = {'form': form}
    return render(request, 'registration/signup.html', context)

def log_in(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect(reverse('todolist'))
    context = {'form': form}
    return render(request, 'registration/login.html', context)
