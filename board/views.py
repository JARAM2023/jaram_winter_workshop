from django.shortcuts import render, redirect
from django.http.response import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from .models import (
    Explain
)

import markdown

def page_index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        index_cont = Explain.objects.get(explain_id='index_cont').explain_text
        index_cont = markdown.markdown(index_cont)
        print(index_cont)
        return render(request, 'index.html', {
            'index_cont': index_cont
        })

def page_login(request):
    if request.user.is_anonymous:
        if 'message' in request.session:
            msg = request.session['message']
            del request.session['message']
            return render(request, 'login.html', {'message': msg})
        return render(request, 'login.html')
    else:
        return redirect('index')

def page_logout(request):
    if request.user.is_anonymous:
        return redirect('login')
    logout(request)
    return redirect('login')

def page_leader(request):
    return render(request, 'leader.html')

def page_team(request):
    return render(request, 'team.html')

def page_submit(request):
    return render(request, 'submit.html')

def form_login(request):
    if request.method == 'POST':
        id = request.POST['text_id']
        password = request.POST['text_password']
        user = authenticate(request, username=id, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            request.session['message'] = '유저가 존재하지 않거나 패스워드가 틀렸습니다.'
            return redirect('login')
    else:
        request.session['message'] = 'request error.'
        return redirect('login')
