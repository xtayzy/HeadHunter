from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

# Create your views here.

from user.forms import SignUpForm, SignInForm


def base(request):
    # if request.user.is_authenticated:
    #     return redirect('index')

    return render(request, 'user/base.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    ctx = {
        'form': SignUpForm(),
    }

    return render(request, 'user/register.html', ctx)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                print('user authenticated')
                login(request, user)
                return redirect('index')
            else:
                print('user is not authenticated')
    form = SignInForm()
    ctx = {
        'form': form
    }
    return render(request, 'user/login.html', context=ctx)


def profile(request):
    user = request.user
    ctx = {
        'user': user
    }
    return render(request, 'user/profile.html', ctx)


def logout_view(request):
    logout(request)

    return redirect('base')