from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from forms import UserEmailForm
from django.contrib.auth.decorators import login_required

@login_required
def update_profile(request):
    if request.method == 'POST':
        form1 = UserProfileForm(request.POST, instance=request.user.profile)
        form2 = UserEmailForm(request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponseRedirect('/profile')
    else:
        user = request.user
        profile = user.profile
        form1 = UserEmailForm(instance=user)
        form2 = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form1'] = form1
    args['form2'] = form2

    return render_to_response('profilePage.html', args)
