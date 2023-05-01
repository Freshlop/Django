from django.shortcuts import HttpResponse, render, redirect
# from datetime import datetime
form products.forms import ProductCreateForm
from posts.models import Product
from products.models import product, Comment

# Create your views here.

'''NVC - MODEL VIEW CONTROLLER'''


# def frist_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Hello! Its my project")


def main_view(request):
    if request.method == 'GET':
       context = {
           'users': request.user
       }
        return render(request, 'layouts/index.html', context=context)


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
            'users': request.user
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        products = Product.objects.get(id=id)

        context = {
            'products': products,
            'comments': products.comment_set.all()
        }

        return render(request, 'posts/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/products.html', context=context)

    if request.method == 'Product':
        data, files=request.PRODUCT, request.FILES
        form =ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleannd.data.get('image'),
                title=form.cleannd.data.get('title'),
                description=form.cleannd.data.get('description'),
                rate=form.cleanned.data.get('rate')
            )


            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


def auth_view(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm
        }