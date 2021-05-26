from django.contrib import admin
from dataapp.models import *
# Register your models here.
class AdminCandidate(admin.ModelAdmin):
    list_display=['name','email','address','first_round','second_round','third_round']
admin.site.register(candidate,AdminCandidate)
