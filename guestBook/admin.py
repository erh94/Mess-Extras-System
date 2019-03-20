from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import GuestBookEntry
from django.contrib.auth import get_user_model

User = get_user_model()
# Register your models here.
# admin.site.register()
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','hostel','hostel_name','first_name','last_name']
    list_filter = ['hostel']

@admin.register(GuestBookEntry)
class GuestBookEntryAdmin(admin.ModelAdmin):
    list_display = ['user','extra','date','cost','quantity','amount']
    list_filter = ['hostel']