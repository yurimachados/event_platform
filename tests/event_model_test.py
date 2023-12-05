import pytest
from django.contrib.auth.models import User
from core.models import Company, Event, Comment

from datetime import datetime
import pytz

@pytest.mark.django_db
def test_event_creation():
    # Cria uma empresa
    company = Company.objects.create(name='Test Company')

    # Cria um evento
    event = Event.objects.create(
        company=company,
        title='Test Event',
        description='This is a test event',
        location='Test Location',
        date=datetime.strptime('2022-01-01T00:00:00Z', '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.UTC)
    )

    # Verifica se o evento foi criado corretamente
    assert event.company == company
    assert event.title == 'Test Event'
    assert event.description == 'This is a test event'
    assert event.location == 'Test Location'
    assert event.date.isoformat() == '2022-01-01T00:00:00+00:00'
    assert event.image == None
    assert event.cover == None

@pytest.mark.django_db
def test_comment_creation():
    # Cria um usuário
    user = User.objects.create_user(username='testuser', password='12345')

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

    # Cria um comentário
    comment = Comment.objects.create(
        event=event,
        user=user,
        text='This is a test comment'
    )

    # Verifica se o comentário foi criado corretamente
    assert comment.event == event
    assert comment.user == user
    assert comment.text == 'This is a test comment'

@pytest.mark.django_db
def test_event_with_comment():
    # Cria um usuário
    user = User.objects.create_user(username='testuser', password='12345')

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

    # Cria um comentário
    comment = Comment.objects.create(
        event=event,
        user=user,
        text='This is a test comment'
    )

    # Verifica se o comentário foi adicionado ao evento
    assert event.comments.first() == comment