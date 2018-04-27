from django.contrib import admin
from .models import UserProfileBasic, PersonalProfile

# Register your models here.
admin.site.register(UserProfileBasic)
admin.site.register(PersonalProfile)
