import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from dashboard.models import Product
from cart import Cart


def home(request):
    product = Product.objects.all()
    return render(request, 'shop/home.html', {'product': product})


class CartView(View):

    def get(self, request, *args, **kwargs):
        cart = Cart(self.request)
        cart = {'items': cart.get_cart()}
        return HttpResponse(json.dumps(cart), content_type='application/json')

    def post(self, request, *args, **kwargs):
        item_id = self.request.POST.get('item_id', 0)
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(self.request)
        cart = {'items': cart.add_item(product)}
        return HttpResponse(json.dumps(cart), content_type='application/json')


def remove_item(request):
    item_id = request.POST.get('item_id', 0)
    print item_id
    product = get_object_or_404(Product, id=item_id)
    cart = Cart(request)
    cart = {'items': cart.delete_item(product)}
    return HttpResponse(json.dumps(cart), content_type='application/json')


def discard_cart(request):
    cart = Cart(request)
    cart.discard_cart()
    return HttpResponse('success')


def increase_item_quantity(request):
    item_id = request.POST.get('item_id', 0)
    product = get_object_or_404(Product, id=item_id)
    cart = Cart(request)
    cart = {'items': cart.increase_item_quantity(product)}
    return HttpResponse(json.dumps(cart), content_type='application/json')


def decrease_item_quantity(request):
    item_id = request.POST.get('item_id', 0)
    product = get_object_or_404(Product, id=item_id)
    cart = Cart(request)
    cart = {'items': cart.decrease_item_quantity(product)}
    return HttpResponse(json.dumps(cart), content_type='application/json')
