from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from profilePage.models import *

def main(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('searchPage.html', c)

def search(request):
	listC = []
	for e in CourseName.objects.all():
		listC.append(e)
	return render_to_response('searchPage.html', {'list': listC})
	


