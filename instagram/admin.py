from django.contrib import admin
from instagram.models import data

# Register your models here.
class admindata(admin.ModelAdmin):
    list_display=("user","pas")

admin.site.register(data,admindata)