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
