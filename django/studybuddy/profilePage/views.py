from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from forms import MyRegistrationForm

def main(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('profilePage.html', c)

def register_user(request):
	if request.method =="POST":
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			auth.login(request, new_user)
			return HttpResponseRedirect('/home/')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()
	args['createmode'] = True
	return render_to_response('profilePage.html', args)

def edit_user(request):
	if request.method =="POST":
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.edit();
			return HttpResponseRedirect('/home/')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()
	args['createmode'] = False 
	return render_to_response('profilePage.html', args)
