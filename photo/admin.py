from django.contrib import admin
from .models import Photo
# Register your models here.



#이거슨 필터 거는거어어어
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'image', 'created', 'updated']
    list_filter = ['author', 'created', 'updated']
    list_fields=['text', 'creatd', 'updated']
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)