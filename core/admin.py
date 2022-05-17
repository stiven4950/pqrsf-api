from django.contrib import admin

from .models import City, Agency, Matter

# Register your models here.
admin.site.register(Matter)
admin.site.register(Agency)
admin.site.register(City)