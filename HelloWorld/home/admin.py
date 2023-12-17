from django.contrib import admin

# Register your models here.
# home/admin.py
from django.contrib import admin
from home.models import UserProfile, Library

admin.site.register(UserProfile)
admin.site.register(Library)