import json
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from dashboard.models import Product
from cart import Cart
from forms import CheckoutForm


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

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cart_items = request.session.get('cart', [])
            total_price = 0
            for item in cart_items:
                total_price += item['price']
            f = form.save(commit=False)
            f.items = json.dumps(cart_items)
            f.total_price = total_price
            f.save()
            data = {
                'name': form.instance.name,
                'address': form.instance.address,
                'email': form.instance.email,
                'city': form.instance.city,
                'pin': form.instance.pin,
                'state': form.instance.state,
                'items': form.instance.get_items,
                'total_price': form.instance.total_price,
                'status': form.instance.status,
                'payment_option': form.instance.payment_option,
                'created': form.instance.created.strftime("%b %d %Y"),
            }
            send_mail(
                'Order placed on shoppingcart',
                'Your order is placed success fully.',
                'kmrvimal@gmail.com',
                ['kriti.cs10@gmail.com'],
                fail_silently=False,
            )
            return HttpResponse(json.dumps(data), content_type='application/json')
            email = form.instance.email

        else:
            return HttpResponse(json.dumps(form.errors), content_type='application/json')
    else:
        form = CheckoutForm()
        return render(request, 'shop/checkout_form.html', {'form': form})
