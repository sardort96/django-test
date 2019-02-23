from django.contrib import admin

from account.models import Schedule


@admin.register(Schedule)
class Admin(admin.ModelAdmin):
    list_display = ['type', 'user', 'from_time', 'to_time']
