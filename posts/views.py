from django.shortcuts import HttpResponse, render
from datetime import datetime

from posts.models import Product

# Create your views here.

'''NVC - MODEL VIEW CONTROLLER'''


def frist_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def main_view(request):
    if request.method == 'GET':
        # return HttpResponse(datetime.datetime.now())
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        # return HttpResponse("Goodbye user!")
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        post = Product.objects.get(id=id)

        context = {
            'post': post
        }

        return render(request, 'posts/detail.html', context=context)
