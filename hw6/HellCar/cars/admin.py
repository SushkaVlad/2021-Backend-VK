from django.contrib import admin

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model')
    list_filter = ('make__name',)
    search_fields = ('make__name', 'model')


admin.site.register(Car, CarAdmin)
