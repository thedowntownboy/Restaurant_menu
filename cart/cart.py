from restaurent_menu.models import Items


class Cart():
    def __init__(self, request):
        self.session = request.session

        # get the current session key if it exists
        cart = self.session.get('session_key')

        # if the user is new and no session ! key create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure cart is available on all page of site
        self.cart = cart

    def add(self, item, item_qty):
        item_id = str(item.id)
        quantity= str(item_qty)
        # logic
        if item_id in self.cart:
            # get cart
            ourcart = self.cart
            # update cart/Dictionary
            ourcart[item_id] = quantity

            self.session.modified = True
        else:
            # self.cart[item_id] = {'price': str(item.price)}
            self.cart[item_id] = int(quantity)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_items(self):
        # get ids from cart
        item_ids = self.cart.keys()

        # use ids to lookup for items in database
        items = Items.objects.filter(id__in=item_ids)
        #items = Items.objects.filter()
        # return those looked up items
        return items

    def get_quantity(self):
        quantities = self.cart
        return quantities

    def update(self, item, quantity):
        item_id = str(item)
        item_qty = int(quantity)

        # get cart
        ourcart = self.cart
        #update cart/Dictionary
        ourcart[item_id] = item_qty

        self.session.modified = True

        thing = self.cart
        return thing


    def delete(self, item):
        # string because session cart is a Dictionary {'4':3,'5':1} 4-id, 3-qty
        item_id = str(item)
        # delete from Dictionary/cart
        if item_id in self.cart:
            del self.cart[item_id]
        self.cart = {}
        self.session.modified = True

    def clearall(self):
        self.cart = self.session['session_key'] = {}
        self.session.modified = True


