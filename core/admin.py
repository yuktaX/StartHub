from django.contrib import admin
from .models import Profile, Startup, Teammember, Tag
# Register your models here.

admin.site.register(Profile)
admin.site.register(Startup)
admin.site.register(Teammember)
admin.site.register(Tag)