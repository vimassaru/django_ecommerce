# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class Payment(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Pay')


class FinishOrder(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Finish View')


class Details(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Details')
