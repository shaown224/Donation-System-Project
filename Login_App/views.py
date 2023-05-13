from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.urls import reverse
from Login_App.forms import SignUpForm, UserProfileChange
from django.contrib.auth.decorators import login_required
# Create your views here.


def sing_up(request):
    form = SignUpForm()
    registerd = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registerd = True

    dict = {'form': form, 'registered': registerd}

    return render(request, 'Login_App/sign_up.html', context=dict)


def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'Login_App/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    return render(request, 'Login_App/profile.html', context={})


@login_required
def user_change(request):
    current_user = request.user

    form = UserProfileChange(instance=current_user)

    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)

    return render(request, 'Login_App/change_proifle.html', context={'form': form})


@login_required
def pass_change(request):
    current_user = request.user

    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if (form.is_valid()):
            form.save()
    return render(request, 'Login_App/pass_change.html', context={'form': form})
