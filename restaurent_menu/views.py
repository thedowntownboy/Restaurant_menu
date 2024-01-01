from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from cart import cart
from .models import Items, MEAL_TYPE
from cart.cart import Cart
from django.http import JsonResponse


class MenuList(generic.ListView):
    queryset = Items.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE

        return context


class MenuItemDetail(generic.DetailView):
    model = Items
    template_name = "menu_item_detail.html"


""" cart functions"""


def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        # get data
        item_id = int(request.POST.get('item_id'))
        item_qty = int(request.POST.get('item_qty'))
        # lookup item in database
        item = get_object_or_404(Items, id=item_id)
        # save to a session
        cart.add(item=item, item_qty=item_qty)
        # get cart quantity
        cart_quantity = cart.__len__()
        # Return response
        #response = JsonResponse({'item ': item.meal})
        response = JsonResponse({'qty': cart_quantity})
        return response


def about(request):
    return render(request, 'about.html')

def order_confirmation(request):
    return render(request, 'order_confirmed.html')
def mybag(request):
    cart = Cart(request)
    cart_items = cart.get_items()
    quantities = cart.get_quantity()
    # Dictionary to store the results
    price = {}
    total_price = 0
    # Multiply dictionary values with corresponding queryset field
    for item in cart_items:
        item_id = str(item.id)
        quantity = quantities.get(item_id, 0)   # Default to 0 if item_id not found in the dictionary
        price[item_id] = float(item.price) * float(quantity)
        total_price += price[item_id]    # Accumulate the total price
        total_price = round(total_price, 2)



    return render(request, 'mybag.html',{'cart_items': cart_items, 'quantities':quantities, 'price':price, 'total_price': total_price})

def cart_update(request):
    # get the cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        # get data
        item_id = str(request.POST.get('item_id'))
        item_qty = int(request.POST.get('item_qty'))
        cart.update(item=item_id, quantity=item_qty)
        response = JsonResponse({'qty':item_qty})
        return response
        #return redirect('mybag')

def cart_delete(request):
    # get the cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        # get data
        item_id = str(request.POST.get('item_id'))
        cart.delete(item=item_id)
        # below code not necessary
        response = JsonResponse({'product': item_id})
        return response


def send(request):
    # get the cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        cart.clearall()

        return JsonResponse({'message': 'Cart cleared successfully'})


