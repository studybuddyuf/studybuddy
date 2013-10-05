from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from forms import MyEditForm
from django.contrib.auth.decorators import login_required

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
	return render_to_response('profilePage.html', args)

@login_required
def edit_user(request):
	if request.method=="POST":
		form = MyEditForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/home/')
	else:
		user = request.user
		profle = user.profile
		form = MyEditForm(instance = user.profile)
	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('editPage.html', args)	
