# flake8: noqa
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from . import models
from . import forms

import copy


class BaseProfile(View):
    template_name = 'userprofile/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.shop_cart = copy.deepcopy(self.request.session.get(
            'shop_cart', {}))
        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.UserProfile.objects.filter(
                user_profile=self.request.user).first()
            self.context = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user,
                ),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None,
                    instance=self.perfil)
            }
        else:
            self.context = {
                'userform': forms.UserForm(
                    data=self.request.POST or None),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None)
            }

        self.userform = self.context['userform']
        self.perfilform = self.context['perfilform']

        self.render_instance = render(
            self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.render_instance


class Create(BaseProfile):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            return self.render_instance

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        # User Logged
        if self.request.user.is_authenticated:
            user_logged = get_object_or_404(
                User, username=self.request.user.username)

            user_logged.username = username

            if password:
                user_logged.set_password(password)

            user_logged.email = email
            user_logged.first_name = first_name
            user_logged.last_name = last_name
            user_logged.save()

        # User Not Logged
        else:
            user_prof = self.userform.save(commit=False)
            user_prof.set_password(password)
            user_prof.save()

            perfil = self.perfilform.save(commit=False)
            perfil.user_profile = user_prof
            perfil.save()

        # User auth
        if password:
            user_auth = authenticate(
                self.request,
                username=username,
                password=password
            )

            if user_auth:
                login(self.request, user=user_logged)

        # Keep the shop_cart with items after change of password
        self.request.session['shop_cart'] = self.shop_cart
        self.request.session.save()

        messages.success(
            self.request,
            'Logged In'
        )

        return redirect('userprofile:create')


class Edit(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Edit')


class LogIn(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(
                self.request,
                'Invalid password or username.',
            )

            return redirect('userprofile:create')

        user_auth = authenticate(
            self.request,
            username=username,
            password=password
        )

        if not user_auth:
            messages.error(
                self.request,
                'Invalid password or username.',
            )
            return redirect('userprofile:create')

        login(self.request, user=user_auth)

        messages.success(
            self.request,
            'Logged In.',
        )

        return redirect('product:shopcart')


class LogOut(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        shop_cart = copy.deepcopy(self.request.session.get('shop_cart'))
        logout(self.request)

        self.request.session['shop_cart'] = shop_cart
        self.request.session.save()

        return redirect('product:list')
