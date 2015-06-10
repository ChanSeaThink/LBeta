from django.contrib import admin
from . import models

#superyang
#123456

class UserAdmin(admin.ModelAdmin):
    list_display = ('UserName','Permission', 'Time')

class ClassOneAdmin(admin.ModelAdmin):
    list_display = ('ClassName','SubClassNum', 'Sequence', 'ProductCount')

class ClassTwoAdmin(admin.ModelAdmin):
    list_display = ('ClassName','PreClass', 'Sequence', 'ProductCount')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('ProductName','ClassOne', 'ClassTwo', 'Sequence')

class ProductPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName','ClassOne', 'ClassTwo', 'Product','Sequence', 'Picture')

admin.site.register(models.User, UserAdmin)
admin.site.register(models.ClassOne, ClassOneAdmin)
admin.site.register(models.ClassTwo, ClassTwoAdmin)
admin.site.register(models.Products, ProductsAdmin)
admin.site.register(models.ProductPic, ProductPicAdmin)