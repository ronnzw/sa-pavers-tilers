from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'subject', 'message')


class FreeQuoteAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname', 'email', 'cell_number', 'address', 'service_req', 'additional_info', 'location')

admin.site.register(Post)
admin.site.register(Newletter)
admin.site.register(FreeQuote, FreeQuoteAdmin)
admin.site.register(Contact, ContactAdmin)
# Register your models here.
