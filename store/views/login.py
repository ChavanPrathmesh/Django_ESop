# for class based views
from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password


# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$390000$oh2oOVPoaOAWD3m8QrbtAe$L2r/cZnCcoKBQ/JCQjNvxcqF8AJHLELBMwFdg9AegDU='))

# Login - class based view
class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                # request.session['customer_email'] = customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = "Email or Password invalid !!"
        else:
            error_message = "Email or Password invalid !!"
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')

# login
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_message = "Email or Password invalid !!"
#         else:
#             error_message = "Email or Password invalid !!"
#         return render(request, 'login.html', {'error': error_message})
