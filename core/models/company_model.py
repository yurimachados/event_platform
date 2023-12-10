from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import Permission, Group

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/company_images/', null=True, blank=True)
    cover = models.ImageField(upload_to='images/company_covers/', null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']

class Manager(AbstractUser):
    username = models.CharField(max_length=255, unique=True, default='manager')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos.")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='managers')
    groups = models.ManyToManyField(Group, related_name='manager_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='manager_user_permissions', blank=True)
    password = models.CharField(max_length=128, default='12345678')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'
        ordering = ['username']