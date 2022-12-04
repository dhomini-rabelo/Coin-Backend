from django.contrib import admin
from backend.bills.app.models import Bill


admin.site.empty_value_display = 'NULL'




@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = 'title', 'bill_type', 'value'
    list_display_links = 'title',
    list_per_page = 50
    ordering = 'title',
    search_fields = 'title',
