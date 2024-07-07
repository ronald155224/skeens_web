from django.contrib import admin
from epaper.models import EPaperEmail, GuestMessage

# Register your models here.
admin.site.register(EPaperEmail)
admin.site.register(GuestMessage)