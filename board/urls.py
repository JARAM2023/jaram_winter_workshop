from django.urls import path, include
from .views import (
    page_index,
    page_login,
    form_login,
    page_logout,
    page_leader,
    page_submit,
    form_submission
)

urlpatterns = [
    path('', page_index, name='index'),
    path('login/', page_login, name='login'),
    path('rank/', page_leader, name='leader'),
    path('submit/', page_submit, name='submit'),
    path('submit/process', form_submission, name='form_submit'),
    path('login/', page_login, name='login'),
    path("login/process/", form_login, name="form_login"),
    path("logout/process/", page_logout, name="logout"),
]