from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Currency(models.Model):
    symbol = models.CharField(max_length=10)
    iso = models.CharField(max_length=3)
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

    def __str__(self):
        return str(self.value)


class TableColumn(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return str(self.value)


class TableSpecification(models.Model):
    title = models.CharField(max_length=255, unique=True)
    rows = models.ManyToManyField(TableRow)
    columns = models.ManyToManyField(TableColumn)

    def __str__(self):
        return self.title


class SurveyCampaign(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    organisations = models.ManyToManyField(Organisation)
    years = models.ManyToManyField(Year)
    tables = models.ManyToManyField(TableSpecification)

    def __str__(self):
        return self.title


class SurveyResponse(models.Model):
    organisation = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, blank=True, null=True, on_delete=models.SET_NULL)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL)
    response = JSONField()
