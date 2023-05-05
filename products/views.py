from django.shortcuts import HttpResponse, render, redirect
# from datetime import datetime
form products.forms import ProductsCreateForm
from products.models import Product
from products.models import products, Comment
from products.constants import PAGINATTION_LIMIT

# Create your views here.

'''NVC - MODEL VIEW CONTROLLER'''


# def frist_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Hello! Its my project")


def main_page_view(request):
    if request.method == 'GET':
       context = {
           'users': request.user
       }
    return render(request, 'layouts/index.html', context=context)


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = products.__len__() / PAGINATTION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page)
        else:
            max_page = round(max_page)

        products = products [PAGINATTION_LIMIT * (page-1): PAGINATTION_LIMIT * page]

       if search:
           products = products.filter(
               Q(title__icontains=search) |
               Q(description__icontains=search))

        context = {
            'products': products,
            'users': request.user,
            'pages': range(1, max_page+1)
        }
         return render(request, 'products/products.html', context=context)


def products_detail_view(request, id):
    if request.method == 'GET':
        products = Product.objects.get(id=id)

        context = {
            'products': products,
            'comments': products.comment_set.all()
        }

        return render(request, 'products/detail.html', context=context)


def products_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/products.html', context=context)

    if request.method == 'POST':
        data, files=request.POST, request.FILES
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


