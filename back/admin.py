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

class ProductInfoPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName','ClassOne', 'ClassTwo', 'Product', 'Picture')

class CacheProductInfoPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName','Picture', 'UserID', 'CreateTime')

class BestProductAdmin(admin.ModelAdmin):
    list_display = ('ProductName','Product', 'ClassOne', 'ClassTwo')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('Title', 'ShortContent', 'LongContent', 'CreateTime', 'CreateDate')

class NewsPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'News', 'Picture')

class CacheNewsPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'UserID', 'Picture')

class JobAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Content')

class CultureAdmin(admin.ModelAdmin):
    list_display = ('Part', 'Content')

class HonorPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'Picture')

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('Content', )

class CaseAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Content', 'Sequence')

class CaseFirstPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'Case', 'Picture')

class CasePicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'Case', 'Picture')

class CacheCasePicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'UserID', 'Picture')

class ShopAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Content', 'Sequence')

class ShopFirstPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'Shop', 'Picture')

class ShopPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'Shop', 'Picture')

class CacheShopPicAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'UserID', 'Picture')

admin.site.register(models.User, UserAdmin)
admin.site.register(models.ClassOne, ClassOneAdmin)
admin.site.register(models.ClassTwo, ClassTwoAdmin)
admin.site.register(models.Products, ProductsAdmin)
admin.site.register(models.ProductPic, ProductPicAdmin)
admin.site.register(models.ProductInfoPic, ProductInfoPicAdmin)
admin.site.register(models.CacheProductInfoPic, CacheProductInfoPicAdmin)
admin.site.register(models.BestProduct, BestProductAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.NewsPic, NewsPicAdmin)
admin.site.register(models.CacheNewsPic , CacheNewsPicAdmin)
admin.site.register(models.Job, JobAdmin)
admin.site.register(models.Culture, CultureAdmin)
admin.site.register(models.HonorPic, HonorPicAdmin)
admin.site.register(models.ContactUs, ContactUsAdmin)
admin.site.register(models.Case, CaseAdmin)
admin.site.register(models.CaseFirstPic, CaseFirstPicAdmin)
admin.site.register(models.CasePic, CasePicAdmin)
admin.site.register(models.CacheCasePic, CacheCasePicAdmin)
admin.site.register(models.Shop, ShopAdmin)
admin.site.register(models.ShopFirstPic, ShopFirstPicAdmin)
admin.site.register(models.ShopPic, ShopPicAdmin)
admin.site.register(models.CacheShopPic, CacheShopPicAdmin)

