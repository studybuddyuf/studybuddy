from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from profilePage.models import *

def main(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('searchPage.html', c)

def search(request):
	listC = {}
	listC['courses'] = CourseName.objects.all()
	return render_to_response('searchPage.html', listC)
	


