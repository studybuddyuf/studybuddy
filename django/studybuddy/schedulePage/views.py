from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect

def main(request):
    return render_to_response('schedulePage.html', {'full_name': request.user.username})

def edit(request):
    return render_to_response('editSchedulePage.html');
