from django.urls import path, include
from .views import (
    page_index,
    page_login,
    form_login
)

urlpatterns = [
    path('', page_index, name='index'),
    path('login/', page_login, name='login'),
    path("login/process/", form_login, name="form_login"),
]