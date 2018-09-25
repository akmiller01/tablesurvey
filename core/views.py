from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user
    return render_to_response('core/home.html', {"user": user})


def login_user(request):
    logout(request)
    nextURL = request.GET.get('next')
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        nextURL = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if nextURL is not None:
                    return HttpResponseRedirect(nextURL)
                else:
                    return HttpResponseRedirect('/')
    return render(request, 'core/login.html', {'next': nextURL})
