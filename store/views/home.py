from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.categories import Category
from django.views import View


# Create your views here.
# def index(request):
#     products = None
#     categories = Category.get_all_categories();
#
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products();
#
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print(request.session.get('customer_email'))
#     return render(request, 'index.html', data)


# Create class based views
class Index(View):

    def get(self, request):

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None

        categories = Category.get_all_categories()

        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        print(request.session.get('customer_email'))
        return render(request, 'index.html', data)

    def post(self, request):
        product_id = request.POST.get('product_id')
        remove = request.POST.get('remove')
        # print(product_id)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')
