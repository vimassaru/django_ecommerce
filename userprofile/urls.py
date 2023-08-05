from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('', views.Create.as_view(), name='create'),
    path('edit/', views.Edit.as_view(), name='edit'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
]
