from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.Payment.as_view(), name='payment'),
    path('finishorder/', views.FinishOrder.as_view(), name='finishorder'),
    path('details/', views.Details.as_view(), name='details'),
]
