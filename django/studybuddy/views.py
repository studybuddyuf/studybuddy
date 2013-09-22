from django.shortcuts import render
from studybuddy.models import User

def hello(request):
    user = User.objects.all()[0]
    return render(request, 'hello.html', {'user': user})
