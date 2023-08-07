from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductList.as_view(), name='list'),
    path('<slug>', views.ProductDetail.as_view(), name='detail'),
    path('addtocart/', views.AddToCart.as_view(), name='addtocart'),
    path('removefromcart/', views.RemoveFromCart.as_view(),
         name='removefromcart'),
    path('shopcart/', views.ShopCart.as_view(), name='shopcart'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('paypal/', include("paypal.standard.ipn.urls"), name='paypal'),
    path('successful/', views.payment_success, name='paypal_success'),
    path('cancelled/', views.payment_cancelled, name='payment_cancelled'),
]
