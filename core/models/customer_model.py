from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import Permission, Group

class Customer(AbstractUser):
    phone_regex = RegexValidator(
        regex   = r'^\+?1?\d{9,15}$',
        message = "O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos.",
        code    = 'invalid_phone'
    )
    phone       = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    cpf_regex   = RegexValidator(
        regex   = r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$',
        message = "O CPF deve estar no formato: '999.999.999-99'.",
        code    = 'invalid_cpf'
    )
    cpf         = models.CharField(validators=[cpf_regex], max_length=14, unique=True)
    birthday    = models.DateField()
    email       = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name='customer_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customer_user_permissions', blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['username']