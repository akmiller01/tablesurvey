from django.contrib import admin
from core.models import Currency, Organisation, Contact, SurveyCampaign, TableRow, TableColumn, TableSpecification, Year


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


class TableRowInline(admin.TabularInline):
    model = TableRow


class TableColumnInline(admin.TabularInline):
    model = TableColumn


class TableSpecificationAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [TableRowInline, TableColumnInline, ]
    save_on_top = True


class YearInline(admin.TabularInline):
    model = Year


class OrganisationInline(admin.TabularInline):
    model = Organisation


class TableSpecificationInline(admin.TabularInline):
    model = TableSpecification


class SurveyCampaignAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    inlines = [OrganisationInline, YearInline, TableSpecificationInline]
    prepopulated_fields = {'slug': ('title',), }
    save_on_top = True


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Contact, ContactAdmin)
