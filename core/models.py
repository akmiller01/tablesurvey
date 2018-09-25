from django.db import models
from django.contrib.auth.models import User


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
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class Year(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return self.value


class TableRow(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class TableColumn(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class TableSpecification(models.Model):
    title = models.CharField(max_length=255, unique=True)
    rows = models.ManyToManyField(TableRow)
    columns = models.ManyToManyField(TableColumn)

    def __str__(self):
        return self.title


class SurveyCampaign(models.Model):
    title = models.CharField(max_length=255, unique=True)
    organisations = models.ManyToManyField(Organisation)
    years = models.ManyToManyField(Year)
    tables = models.ManyToManyField(TableSpecification)

    def __str__(self):
        return self.title
