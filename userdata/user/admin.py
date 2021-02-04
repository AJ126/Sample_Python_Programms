from django.contrib import admin
from user.models import *
# Register your models here.
class userinfoAdmin(admin.ModelAdmin):
    list_display=['name','username','password','street','pincode','country','state','phoneno']
admin.site.register(userinfo,userinfoAdmin)
