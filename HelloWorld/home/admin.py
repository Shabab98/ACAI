#from django.contrib import admin

# Register your models here.
# home/admin.py
#from django.contrib import admin
#from home.models import UserProfile, Library

#admin.site.register(UserProfile)
#admin.site.register(Library)


from django.contrib import admin
from .models import Library

# Register your models here.
#@admin.register(Library)
#class LibraryAdmin(admin.ModelAdmin):
#    pass
admin.site.register(Library)