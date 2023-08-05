from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

from utils.usa_states import states


"""
UserProfile:
    user: FK user (ou OneToOne)
    age: Int
    data_nascimento: Date
    cpf: char
    endereco: char
    numero: char
    complemento: char
    bairro: char
    cep: Char
    cidade: char
    estado: Choices
        usa_states_tuple
"""


class UserProfile(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()
    ssn = models.CharField(
        max_length=12,
        verbose_name='SSN'
    )
    address_location = models.CharField(max_length=50)
    address_number = models.CharField(max_length=5)
    extra_description = models.CharField(
        max_length=30,
        blank=True,
    )
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    city_state = models.CharField(
        max_length=2,
        default=None,
        blank=True,
        choices=(
            states
        )
    )

    def __str__(self) -> str:
        return f'{self.user_profile}'

    def clean(self):
        # Validating and Raising Errors Messages
        error_messages = {}

        # TODO: create a ssn validation

        # TODO: create a validation for zipcode

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
