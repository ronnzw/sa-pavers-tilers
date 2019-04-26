from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'subject', 'message')

admin.site.register(Post)
admin.site.register(Newletter)
admin.site.register(FreeQuote)
admin.site.register(Contact, ContactAdmin)
# Register your models here.
