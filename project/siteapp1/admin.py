from django.contrib import admin
from siteapp1.models import uploadData
from siteapp1.models import siteusers

# Register your models here.

admin.site.register(siteusers)
admin.site.register(uploadData)
