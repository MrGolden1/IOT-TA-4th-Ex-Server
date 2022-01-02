from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as django_UserAdmin
from .models import User
from rest_framework.authtoken.models import Token

# Register your models here.



@admin.register(User)
class UserAdmin(django_UserAdmin):

    list_display =  ['id','first_name','last_name','chipID','studentID','expression','solution','created','updated']
    exclude = []
    ordering = ()

# @admin.register(Token)
# class TokenAdmin(admin.ModelAdmin):
#     pass