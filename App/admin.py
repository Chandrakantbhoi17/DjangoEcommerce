from pyexpat import model
from django.contrib import admin
from django.http import HttpResponse
from .models import  UserDetail,EmailOtp
@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_diplay="__all__"


@admin.register(EmailOtp)
class EmailOtpAdmin(admin.ModelAdmin):
    list_display=['user','otp']

    




