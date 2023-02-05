from django.shortcuts import render, redirect

def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')
