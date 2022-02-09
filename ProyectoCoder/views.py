from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from ProyectoCoder.forms import UserRegisterForm
from django.contrib.auth.models import User
import django


def login_request (request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.data.get('username')
            passwd = form.data.get('password')

            user = authenticate(username=usuario, password=passwd)

            if user:
                login(request, user)

                return redirect('List')
            else:
                return redirect('New')

        else:
            return redirect('New')

    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.data['username']
            try:
                user_new = User.objects.get(username=username)
            except django.contrib.auth.models.User.DoesNotExist:
                user_new = None
            
            if not user_new:

                form.save()

            return redirect('Login')

    else:
        print('asdfasdfadsf')        
        # form = UserCreationForm()
        form = UserRegisterForm(request.POST)

    return render(request, 'register.html', {'form': form})
