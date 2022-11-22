from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    fields = ("name", "email")
    list_display = ("name", "email", 'type', 'created_at', 'updated_at')
    list_display_links = ("name",)
    search_fields = ("name", "email")




admin.site.register(Customer, CustomerAdmin)
