from django.contrib import admin
from core.models import *


class ContactInline(admin.TabularInline):
    model = Contact


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ContactInline, ]
    prepopulated_fields = {'slug': ('name',), }
    save_on_top = True


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['iso', 'description', 'symbol']
    save_on_top = True


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'organisation']
    def name(self, obj):
        return obj.user.get_full_name()
    save_on_top = True


class TableSpecificationAdmin(admin.ModelAdmin):
    list_display = ['title']
    save_on_top = True


class SurveyCampaignAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    prepopulated_fields = {'slug': ('title',), }
    save_on_top = True


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(TableSpecification, TableSpecificationAdmin)
admin.site.register(SurveyCampaign, SurveyCampaignAdmin)
admin.site.register(TableRow)
admin.site.register(TableColumn)
admin.site.register(Year)
admin.site.register(SurveyResponse)
