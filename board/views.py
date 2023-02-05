from django.shortcuts import render

def index(request):
    print(request.user.is_superuser)
    return render(request, 'index.html')
