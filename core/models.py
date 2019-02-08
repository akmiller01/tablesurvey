from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.urls import reverse


class Currency(models.Model):
    symbol = models.CharField(max_length=10)
    iso = models.CharField(max_length=3, unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['iso']
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.iso


class Organisation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    organisation = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.get_full_name()


class Year(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

class TableRow(models.Model):
    value = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.organisation:
            return("{} ({})".format(self.value, self.organisation.name))
        return str(self.value)


class TableColumn(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return str(self.value)


class TableSpecification(models.Model):
    title = models.CharField(max_length=255, unique=True)
    rows = models.ManyToManyField(TableRow)
    columns = models.ManyToManyField(TableColumn)
    allow_user_rows = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SurveyCampaign(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    organisations = models.ManyToManyField(Organisation)
    years = models.ManyToManyField(Year)
    tables = models.ManyToManyField(TableSpecification)
    instructions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core.views.edit", args=[self.slug])


class SurveyResponse(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    campaign = models.ForeignKey(SurveyCampaign, blank=True, null=True, on_delete=models.SET_NULL)
    table = models.ForeignKey(TableSpecification, blank=True, null=True, on_delete=models.SET_NULL)
    organisation = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, blank=True, null=True, on_delete=models.SET_NULL)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL)
    row = models.ForeignKey(TableRow, blank=True, null=True, on_delete=models.SET_NULL)
    column = models.ForeignKey(TableColumn, blank=True, null=True, on_delete=models.SET_NULL)
    value = models.CharField(max_length=255, blank=True, null=True)

    def coordinates(self):
        return "|".join([str(self.table.title), str(self.row.value), str(self.column.value)])
