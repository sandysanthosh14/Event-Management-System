from django.contrib import admin
from .models import EventCategory,Event,membership,Event_join

# Register your models here.
#class EventAdmin(admin.ModelAdmin):
    # other configurations...
    #list_display = ('title', 'location', 'date') 
admin.site.register(EventCategory)

admin.site.register(Event)
admin.site.register(membership)
admin.site.register(Event_join)


