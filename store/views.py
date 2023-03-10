import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def Store(request):
    if request.user.is_authenticated:
        coustomer = request.user.coustomer
        order, created = Order.objects.get_or_create(coustomer=coustomer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']



    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def Cart(request):
    if request.user.is_authenticated:
        coustomer = request.user.coustomer
        order, created = Order.objects.get_or_create(coustomer=coustomer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        coustomer = request.user.coustomer
        order, created = Order.objects.get_or_create(coustomer=coustomer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:', productId)


    coustomer = request.user.coustomer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(coustomer=coustomer, complete=False)

    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('item was added', safe=False)




