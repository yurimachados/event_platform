from django.contrib import admin
from .models import Event, Ticket, Company, Comment, Rating

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Company)
admin.site.register(Comment)
admin.site.register(Rating)