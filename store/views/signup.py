# validation for singup form
# def validateCustomer(customer, confpassword):
#     # Validation
#     error_message = None
#     if not customer.first_name:
#         error_message = "First Name required !!"
#     elif len(customer.first_name) < 3:
#         error_message = "First Name must be 3 char long or more"
#     elif not customer.last_name:
#         error_message = "Last Name required !!"
#     elif len(customer.last_name) < 4:
#         error_message = "Last Name must be 3 char long or more"
#     elif not customer.phone:
#         error_message = "Phone Number required !!"
#     elif len(customer.phone) < 10:
#         error_message = "Phone Number must be 10 char long"
#     elif not customer.email:
#         error_message = "Email required !!"
#     elif len(customer.email) < 4:
#         error_message = "Enter correct email !!"
#     elif not customer.password:
#         error_message = "Password required !!"
#     elif len(customer.password) < 8:
#         error_message = "Password must be 8 char long or more"
#     elif not confpassword:
#         error_message = "Confirm password required !!"
#     elif customer.password != confpassword:
#         error_message = "Password doesn't match !!"
#     elif Customer.objects.filter(phone=customer.phone):
#         error_message = "Phone Number Already registered !!"
#     elif customer.isExists():
#         error_message = "Email Already registered !!"
#
#     return error_message


# signup post method
# def registerUser(request):
#     postData = request.POST
#     first_name = postData.get('firstname')
#     last_name = postData.get('lastname')
#     phone = postData.get('phone')
#     email = postData.get('email')
#     password = postData.get('password')
#     confpassword = postData.get('confpassword')
#
#     value = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'phone': phone,
#         'email': email,
#     }
#     # Customer Object
#     customer = Customer(first_name=first_name,
#                         last_name=last_name,
#                         phone=phone,
#                         email=email,
#                         password=password)
#     error_message = validateCustomer(customer, confpassword)
#     # Saving
#     if not error_message:
#         customer.password = make_password(customer.password)
#         customer.register()
#         return redirect('homepage')
#     else:
#         data = {
#             'error': error_message,
#             'values': value,
#         }
#         return render(request, 'signup.html', data)


# singup - class based view
# for class based views
from django.views import View
from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password


class Singup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        confpassword = postData.get('confpassword')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        # Customer Object
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer, confpassword)
        # Saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer, confpassword):
        # Validation
        error_message = None
        if not customer.first_name:
            error_message = "First Name required !!"
        elif len(customer.first_name) < 3:
            error_message = "First Name must be 3 char long or more"
        elif not customer.last_name:
            error_message = "Last Name required !!"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 3 char long or more"
        elif not customer.phone:
            error_message = "Phone Number required !!"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 char long"
        elif not customer.email:
            error_message = "Email required !!"
        elif len(customer.email) < 4:
            error_message = "Enter correct email !!"
        elif not customer.password:
            error_message = "Password required !!"
        elif len(customer.password) < 8:
            error_message = "Password must be 8 char long or more"
        elif not confpassword:
            error_message = "Confirm password required !!"
        elif customer.password != confpassword:
            error_message = "Password doesn't match !!"
        elif Customer.objects.filter(phone=customer.phone):
            error_message = "Phone Number Already registered !!"
        elif customer.isExists():
            error_message = "Email Already registered !!"

        return error_message

# signup get method
# def signup(request):
#     # print(request.method)
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return registerUser(request)
