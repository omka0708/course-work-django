from django.contrib import admin

from .models import Ticket, Event


class TicketAdmin(admin.ModelAdmin):
    list_display = ('idticket', 'first_name', 'last_name', 'type', 'event_idevent', 'email')
    search_fields = ('first_name', 'last_name')


class EventAdmin(admin.ModelAdmin):
    list_display = ('idevent', 'title', 'date')
    list_display_links = ('idevent', 'title')
    search_fields = ('title',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Event, EventAdmin)
