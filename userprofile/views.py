# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class Create(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Create')


class Edit(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Edit')


class LogIn(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Log In')


class LogOut(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Log Out')
