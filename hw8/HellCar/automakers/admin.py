from django.contrib import admin
from automakers.models import AutoMaker


class AutomakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('location', )
    search_fields = ('name',)


admin.site.register(AutoMaker, AutomakerAdmin)
