from django.urls import path
from . import views


urlpatterns = [
    path('', views.Store, name='store' ),
    path('checkout/', views.checkout, name= 'checkout' ),
    path('cart/', views.Cart, name='cart'),
    path('update_item/', views.UpdateItem, name='update-item')

]
