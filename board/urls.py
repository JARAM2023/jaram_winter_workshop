from django.urls import path, include
from .views import (
    page_index,
    page_login,
    form_login,
    page_logout,
    page_leader,
    page_submit,
    form_submission,
    form_leader,
    page_change_password,
    form_change_password
)

urlpatterns = [
    path('', page_index, name='index'),
    path('login/', page_login, name='login'),
    path('rank/', page_leader, name='leader'),
    path('rank/process/', form_leader, name='form_leader'),
    path('submit/', page_submit, name='submit'),
    path('submit/process/', form_submission, name='form_submit'),
    path('login/', page_login, name='login'),
    path("login/process/", form_login, name="form_login"),
    path("logout/process/", page_logout, name="logout"),
    path("accout/", page_change_password, name="password_change"),
    path("accout/process", form_change_password, name="form_password_change"),
]