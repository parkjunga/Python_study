from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',) #,를써야 튜플로 인식

admin.site.register(Fcuser, FcuserAdmin)