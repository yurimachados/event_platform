from django.db import models
from django.contrib.auth.models import User
from .event_model import Event

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    buyers = models.ManyToManyField(User, related_name='purchased_tickets', blank=True)

    def __str__(self):
        return f"{self.event.title} - {self.name} - R$ {self.price}"