from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contacts
from .models import FormData

admin.site.register(Contacts)
admin.site.register(FormData)
