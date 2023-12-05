import pytest
from django.contrib.auth.models import User
from core.models import Company, Event, Ticket

@pytest.mark.django_db
def test_ticket_creation():
    # Cria uma empresa
    company = Company.objects.create(name='Test Company')

    # Cria um evento
    event = Event.objects.create(
        company=company,
        title='Test Event',
        description='This is a test event',
        location='Test Location',
        date='2022-01-01T00:00:00Z'
    )

    # Cria um ticket
    ticket = Ticket.objects.create(
        event=event,
        name='Test Ticket',
        price=100.00
    )

    # Verifique se o ticket foi criado corretamente
    assert ticket.event == event
    assert ticket.name == 'Test Ticket'
    assert ticket.price == 100.00

@pytest.mark.django_db
def test_ticket_str():
    # Cria uma empresa
    company = Company.objects.create(name='Test Company')

    # Cria um evento
    event = Event.objects.create(
        company=company,
        title='Test Event',
        description='This is a test event',
        location='Test Location',
        date='2022-01-01T00:00:00Z'
    )

    # Cria um ticket
    ticket = Ticket.objects.create(
        event=event,
        name='Test Ticket',
        price=100.00
    )

    # Verifica a representação em string do ticket
    assert str(ticket) == 'Test Event - Test Ticket - R$ 100.0'