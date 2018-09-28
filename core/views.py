from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import SurveyCampaign, Contact, Currency, SurveyResponse, TableSpecification, TableRow, TableColumn
from csv import writer as csvwriter


@login_required
def edit(request, slug, year=None):
    messages = []
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
        if campaign.active:
            currency_iso = request.POST.get('currency')
            if currency_iso:
                currency = Currency.objects.filter(iso=currency_iso).first()
            else:
                currency = None
            exclude_keys = ["currency", "csrfmiddlewaretoken"]
            for key, value in request.POST.items():
                if key not in exclude_keys:
                    split_coords = key.split("|")
                    table_title = split_coords[0]
                    row_value = split_coords[1]
                    column_value = split_coords[2]
                    table = TableSpecification.objects.filter(title=table_title).first()
                    row = TableRow.objects.filter(value=row_value).first()
                    column = TableColumn.objects.filter(value=column_value).first()
                    response, _ = SurveyResponse.objects.get_or_create(
                        campaign=campaign,
                        table=table,
                        organisation=organisation,
                        year=year,
                        row=row,
                        column=column
                    )
                    response.currency = currency
                    response.value = str(value)
                    response.save()
            messages.append("Your response has been successfully submitted.")
        else:
            messages.append("Sorry, this campaign is no longer accepting responses.")
    responses = SurveyResponse.objects.filter(
        campaign=campaign,
        organisation=organisation,
        year=year
    )
    if responses:
        currency = responses.first().currency
    else:
        currency = None
    return render(
        request,
        'core/edit.html',
        {
            "user": user,
            "organisation": organisation,
            "campaign": campaign,
            "year": year,
            "years": years,
            "currencies": currencies,
            "responses": responses,
            "currency": currency,
            "messages": messages
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


@login_required
def export(request, slug=None):
    user = request.user
    contact = get_object_or_404(Contact, user=user)
    organisation = contact.organisation
    if user.is_staff:
        if slug is None:
            survey_responses = SurveyResponse.objects.all()
        else:
            survey_responses = SurveyResponse.objects.filter(organisation__slug=slug)
    else:
        if slug is None:
            survey_responses = SurveyResponse.objects.filter(organisation__slug=organisation.slug)
        else:
            survey_responses = SurveyResponse.objects.filter(organisation__slug=slug)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csvwriter(response)
    header = [
        "timestamp",
        "updated",
        "campaign_title",
        "campaign_active",
        "table",
        "organisation",
        "year",
        "currency",
        "row",
        "column",
        "value"
    ]
    writer.writerow(header)
    for survey_response in survey_responses:
        writer.writerow([
            survey_response.timestamp.strftime("%Y-%m-%d %H:%M"),
            survey_response.updated.strftime("%Y-%m-%d %H:%M"),
            survey_response.campaign.title,
            survey_response.campaign.active,
            survey_response.table.title,
            survey_response.organisation.name,
            survey_response.year.value,
            survey_response.currency.iso if survey_response.currency else "",
            survey_response.row.value,
            survey_response.column.value,
            survey_response.value
        ])
    return response
