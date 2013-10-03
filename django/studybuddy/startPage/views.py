from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf

def main(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('startPage.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/home' )
    else:
        return render(request, 'startPage.html', {'errors':True})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')




