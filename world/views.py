from django.shortcuts import render


def index(request):
    pass
    return render(request, 'polls/index.html')
