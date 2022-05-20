from django.contrib import admin

from .models import City, Agency, Matter, FileUser, UserPqrsf

# Register your models here.
admin.site.register(Matter)
admin.site.register(Agency)
admin.site.register(City)
admin.site.register(FileUser)
admin.site.register(UserPqrsf)