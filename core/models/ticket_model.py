import secrets
from django.db import models
from django.contrib.auth.models import User
from .event_model import Event
from .customer_model import Customer

class Ticket(models.Model):
    event               = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    name                = models.CharField(max_length=255)
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    available           = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.event.title} - {self.name} - R$ {self.price}"
    
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['event', 'name']
    
class TicketPurchase(models.Model):
    ticket              = models.ForeignKey(Ticket, on_delete=models.PROTECT, related_name='purchases', null=True)
    ticket_name         = models.CharField(max_length=255, blank=True)
    ticket_price        = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    buyer               = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='ticket_purchases')
    code                = models.CharField(max_length=8, unique=True, blank=True)
    date                = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = secrets.token_hex(4).upper()
        if not self.ticket_name:
            self.ticket_name = self.ticket.name
        if not self.ticket_price:
            self.ticket_price = self.ticket.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket.event.title} - {self.ticket.name} - {self.buyer.username} - R$ {self.ticket_price}"  
    
    class Meta:
        verbose_name = 'Ticket Purchase'
        verbose_name_plural = 'Ticket Purchases'
        ordering = ['ticket_name', 'buyer', 'date']