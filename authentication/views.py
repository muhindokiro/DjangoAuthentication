from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'registration/index.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data['password']
                messages.success(request, 'Account was created for ' + username)


                # user = authenticate(username=username, password=password)
                # login(request, user)
                return redirect('login')
        # else:
            # form = CreateUserForm()

        context = {'form' : form}
        return render(request, 'registration/register.html', context)   


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)   


def logoutUser(request):
    logout(request)
    return redirect('login')