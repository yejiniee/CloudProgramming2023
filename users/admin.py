from django.contrib import admin
from .models import Profile

'''
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Users, UsersAdmin)
'''
admin.site.register(Profile)