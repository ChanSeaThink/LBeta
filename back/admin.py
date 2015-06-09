from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('UserName','Permission', 'Time')

class ClassOneAdmin(admin.ModelAdmin):
    list_display = ('ClassName','SubClassNum', 'Sequence', 'ProductCount')

class ClassTwoAdmin(admin.ModelAdmin):
    list_display = ('ClassName','PreClass', 'Sequence', 'ProductCount')

admin.site.register(models.User, UserAdmin)
admin.site.register(models.ClassOne, ClassOneAdmin)
admin.site.register(models.ClassTwo, ClassTwoAdmin)