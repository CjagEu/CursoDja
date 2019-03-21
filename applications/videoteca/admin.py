from django.contrib import admin

from .models import Bboy, Powermove

#Clase para mejorar la pagina admin de Bboy
class BboyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nacionalidad',
        'id'
    )
    search_fields = ('name','nacionalidad',)

#Clase para mejorar la pagina admin de Powermove
class PowermoveAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'resume',
        'id',
    )
    search_fields = ('name',)
    list_filter = ('bboy',)








# Register your models here.
admin.site.register(Bboy,BboyAdmin)
admin.site.register(Powermove,PowermoveAdmin)