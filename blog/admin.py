from django.contrib import admin
from .models import *
# Register your models here.


class Adminpepole(admin.ModelAdmin):   
    list_display = ('mobile_name', 'slug', 'desc', 'image', 'price', 'status', 'prcs')            #serch bar asase che bashad
    prepopulated_fields = {'slug':('mobile_name',)}
    list_filter = ('status', 'publication_blog','cate')


class lobtopadmiv(admin.ModelAdmin):           
    list_display = ('labtop_name', 'slug', 'desc', 'image', 'price', 'status')      #serch bar asase che bashad
    prepopulated_fields = {'slug':('labtop_name',)}
    list_filter = ('status' , 'publication_blog', 'cate')


class postadmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'desc', 'status')
    list_filter = ('publish' , 'status')                      #list filter
    search_fields = ('publish' , 'title')               #serch bar asase che bashad
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status' , 'publish']


class procer(admin.ModelAdmin):               #serch bar asase che bashad
    list_display = ('chip', 'graphic_chip', 'information', 'slug')
    prepopulated_fields = {'slug': ('chip', 'graphic_chip')}


class body(admin.ModelAdmin):
    list_display = ('body_material', 'dimensions', 'weight', 'slug')


class body_lab(admin.ModelAdmin):
    list_display = ('body_material', 'information', 'weight', 'slug')


class connect(admin.ModelAdmin):
    list_display = ('usb', 'type_c', 'hdmi')



class cater(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(mobile, Adminpepole)
admin.site.register(labtop, lobtopadmiv)
admin.site.register(category, cater)
admin.site.register(category_obshen)
admin.site.register(mobile_screen)
admin.site.register(camera)
admin.site.register(color)
admin.site.register(mobile_body, body)
admin.site.register(processor, procer)
admin.site.register(memory)
admin.site.register(speaker)
admin.site.register(labtop_body, body_lab)
admin.site.register(connections_labtop, connect)
admin.site.register(post, postadmin)
admin.site.register(User)