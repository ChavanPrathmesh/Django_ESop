from django.views import View
from django.shortcuts import render
from store.models.order import Order
from store.middlewares.auth import auth_middleware


class Orders(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})
