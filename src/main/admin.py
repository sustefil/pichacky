from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Place, User, Action

admin.site.register(Place)
admin.site.register(User)
admin.site.register(Action)
