from django.contrib import admin
from .models import Contact


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date', 'phone')
    list_display_links = ('id', 'name', 'listing')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactsAdmin)
