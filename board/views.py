from django.shortcuts import render, redirect
from django.http.response import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from .models import (
    Explain,
    Team,
    SubmitResult,
    LeaderBoard
)

import markdown
import pandas
import os
import io

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
                last_submit = f'{last_submit.day}일 {last_submit.hour}시 {last_submit.minute}분 {last_submit.second}초'
            else:
                last_submit = None
            team_users.append({'name': name, 'last_submit': last_submit})

        team_sub_log = SubmitResult.objects.filter(submit_team_pk=request.user.team_user.all()[0])
        team_sub_log = team_sub_log.order_by('-submit_score')
        team_submit = []
        for l in team_sub_log:
            create_time = l.submit_create
            create_time = f'{create_time.day}일 {create_time.hour}시 {create_time.minute}분 {create_time.second}초'
            is_selected = LeaderBoard.objects.filter(leader_submit_pk=l)
            if is_selected:
                is_selected = True
            else:
                is_selected = False
            team_submit.append({
                'sub_num': l.submit_pk,
                'file_name': l.submit_name,
                'submitter': l.submit_user_pk.username,
                'score': l.submit_score,
                'create_time': create_time,
                'is_selected': is_selected
            })

        context = {
            'team_users': team_users,
            'submit_log': team_submit
        }
        if 'message' in request.session:
            context['message'] = request.session['message']
            del request.session['message']

        return render(request, 'submit.html', context)

def form_submission(request):
    if request.user.is_anonymous:
        return redirect('login')
    elif request.method == 'POST' and request.FILES['file_data']:
        file = request.FILES['file_data']
        real_name = file.name
        change_name = get_random_string(20)
        while os.path.exists(f'./media/submits/{change_name}'):
            change_name = get_random_string(20)
        file.name = change_name

        try:
            answer = pandas.read_csv('./static/new_weather_data_test_y.csv', index_col=0)
            submission = pandas.read_csv(io.StringIO(request.FILES['file_data'].read().decode('utf-8')), index_col=0)
            assert answer.shape == submission.shape

            answer = answer['weather'].values
            submission = submission['weather'].values
            submit_score = sum(answer == submission) / len(answer)
        except:
            request.session['message'] = '파일 제출 과정에서 오류가 발생했습니다.'
            return redirect('submit')

        sub = SubmitResult(
            submit_file=request.FILES['file_data'],
            submit_team_pk=request.user.team_user.all()[0],
            submit_name=real_name,
            submit_user_pk=request.user,
            submit_score=submit_score
        )
        sub.save()
        return redirect('submit')
    else:
        return redirect('submit')

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
