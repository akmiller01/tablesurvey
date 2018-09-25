from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import SurveyCampaign, Contact, Currency


@login_required
def edit(request, slug, year=None):
    user = request.user
    contact = get_object_or_404(Contact, user=user)
    organisation = contact.organisation
    campaign = get_object_or_404(SurveyCampaign, slug=slug)
    years = campaign.years.order_by('value').all()
    currencies = Currency.objects.all()
    if not year:
        year = campaign.years.first()
    else:
        year = int(year)
    if request.method == "POST":
        pass
    else:
        pass
    return render(
        request,
        'core/edit.html',
        {
            "user": user,
            "organisation": organisation,
            "campaign": campaign,
            "year": year,
            "years": years,
            "currencies": currencies
        }
    )


@login_required
def index(request):
    user = request.user
    contact = get_object_or_404(Contact, user=user)
    active_campaigns = SurveyCampaign.objects.filter(
        organisations__pk=contact.organisation.pk,
        active=True
    )
    return render_to_response('core/home.html', {"user": user, "active_campaigns": active_campaigns})


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
