from django.contrib import admin
from .models import PollingInstitute

@admin.register(PollingInstitute)
class PollingInstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'established_year')
    search_fields = ('name', 'location')
    list_filter = ('established_year',)  # ← Correct
