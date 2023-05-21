from django.contrib import admin
from cinemas.models import Cinema, Room, Seat, Showtime, Ticket

admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Showtime)
admin.site.register(Ticket)