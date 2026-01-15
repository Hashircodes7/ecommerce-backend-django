from django.contrib import admin
from accounts.models import Profile,User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class user_register(UserAdmin):
    list_display=['first_name','last_name','email','username','is_staff']
    search_fields=['username','first_name','last_name']

@admin.register(Profile)
class profile_register(admin.ModelAdmin):
    list_display=['user','avatar','bio']