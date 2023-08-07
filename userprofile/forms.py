# flake8: noqa
from django import forms
from django.contrib.auth.models import User

from . import models


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        exclude = ('user_profile',)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
    )

    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
    )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password', 'password2', 'email')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_messages = {}

        user_data = cleaned.get('username')
        user_email = cleaned.get('email')
        user_password = cleaned.get('password')
        user_password2 = cleaned.get('password2')

        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=user_email).first()

        error_msg_user_exists = "User already exists."
        error_msg_email_exists = "E-mail already exists."
        error_msg_password_match = "Password does not match."
        error_msg_password_short = "Password is too short, try with at least 6 characters."

        if self.user:
            if user_data != user_db.username:
                if user_db:
                    validation_error_messages['username'] = error_msg_user_exists

            # if user_email != email_db.username:
            #     if email_db:
            #         validation_error_messages['email'] = error_msg_email_exists

            if user_password:
                if user_password != user_password2:
                    validation_error_messages['password'] = error_msg_password_match
                    validation_error_messages['password2'] = error_msg_password_match

                if len(user_password) < 6:
                    validation_error_messages['password'] = error_msg_password_short

        else:
            if user_db:
                validation_error_messages['username'] = error_msg_user_exists

            if email_db:
                validation_error_messages['email'] = error_msg_email_exists

            if user_password != user_password2:
                validation_error_messages['password'] = error_msg_password_match
                validation_error_messages['password2'] = error_msg_password_match

            if len(user_password) < 6:
                validation_error_messages['password'] = error_msg_password_short

        if validation_error_messages:
            raise (forms.ValidationError(validation_error_messages))
