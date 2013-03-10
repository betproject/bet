from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from users.forms import RegistrationForm, LoginForm
from users.models import Userbet
from django.contrib.auth import authenticate, login, logout

def UserbetRegistration(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/user/')
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
                        user.save()
                        userbet = Userbet(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
                        userbet.save()
                        return HttpResponseRedirect('/user/')
                else:
                        return render_to_response('users/register.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show them a blank registration form '''
                form = RegistrationForm()
                context = {'form': form}
                return render_to_response('users/register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/user/')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        userbet = authenticate(username=username, password=password)
                        if userbet is not None:
                                login(request, userbet)
                                return HttpResponseRedirect('/user/')
                        else:
                                return render_to_response('users/login.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('users/login.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('users/login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('http://127.0.0.1:8000')
		
@login_required
def user(request):
        if not request.user.is_authenticated():
                return HrttpResponseRedirect('/login/')
        userbet = request.user.get_profile
        context = {'userbet': userbet}
        return render_to_response('users/user.html', context, context_instance=RequestContext(request))
		