import pytest
from django.contrib.auth.models import User
from core.models import Company, Manager

@pytest.mark.django_db
def test_manager_creation():
    # Crie um usuário
    user = User.objects.create_user(username='testuser', password='12345')

    # Crie uma empresa
    company = Company.objects.create(name='Test Company')

    # Crie um gerente
    manager = Manager.objects.create(user=user, company=company)

    # Verifique se o gerente foi criado corretamente
    assert manager.user == user
    assert manager.company == company

@pytest.mark.django_db
def test_company_creation():
    # Crie uma empresa
    company = Company.objects.create(
        name='Test Company',
        description='This is a test company',
        location='Test Location'
    )

    # Verifique se a empresa foi criada corretamente
    assert company.name == 'Test Company'
    assert company.description == 'This is a test company'
    assert company.location == 'Test Location'
    assert company.image == None
    assert company.cover == None

@pytest.mark.django_db
def test_company_with_manager():
    # Crie um usuário
    user = User.objects.create_user(username='testuser', password='12345')

    # Crie uma empresa
    company = Company.objects.create(name='Test Company')

    # Crie um gerente
    manager = Manager.objects.create(user=user, company=company)

    # Verifique se o gerente foi adicionado à empresa
    assert company.managers.first() == manager