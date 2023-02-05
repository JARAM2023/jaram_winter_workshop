from django.shortcuts import render, redirect
from django.http.response import HttpResponseBadRequest
from django.contrib.auth import authenticate, login

def page_index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'index.html')

def page_login(request):
    return render(request, 'login.html')

def form_login(request):
    if request.method == 'POST':
        id = request.POST['']
    else:
        return render(request, 'login.html', {'message': 'request error'})
