from django.shortcuts import render

def index(request):
    print(11)
    return render(request, 'index.html')
