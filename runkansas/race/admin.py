from django.contrib import admin
from runkansas.race.models import Race, Distance, Event

class EventInline(admin.TabularInline):
    model = Event
    extra = 0

class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [EventInline,]
    list_display = ('name', 'date', 'contact_name', 'contact_phone', 'contact_email',)
    list_filter = ('date',)
    
class DistanceAdmin(admin.ModelAdmin):
    pass
    
class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Race, RaceAdmin)
admin.site.register(Distance, DistanceAdmin)
admin.site.register(Event, EventAdmin)