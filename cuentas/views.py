from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def logOut(request):
    logout(request)
    return redirect('iniciarSesion')


def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar.html', {
                'form': AuthenticationForm,
                'error': 'Datos incorrectos'
            })
        else:
            login(request, user)
            return redirect('homePage')

@login_required
def homePage(request):

    return render(request, 'home.html')

