from django.shortcuts import render, redirect
from django.http.response import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from .models import (
    Explain,
    Team,
SubmitResult
)

import markdown

def page_index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        index_cont = Explain.objects.get(explain_id='index_cont').explain_text
        index_data = Explain.objects.get(explain_id='index_data').explain_text
        index_cont = markdown.markdown(index_cont)
        index_data = markdown.markdown(index_data)
        return render(request, 'index.html', {
            'index_cont': index_cont,
            'index_data': index_data
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
    if request.user.is_anonymous:
        return redirect('login')
    else:
        team_instance = request.user.team_user.all()[0]
        team_users = []
        for u in team_instance.team_member.all():
            name = u.username
            last_submit = u.submit_user.all().order_by('-submit_create')
            if last_submit:
                last_submit = last_submit[0].submit_create
            else:
                last_submit = None
            team_users.append({'name': name, 'last_submit': last_submit})
        return render(request, 'submit.html', {
            'team_users': team_users
        })

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
