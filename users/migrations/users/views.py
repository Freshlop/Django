from django.shortcuts import render
from  django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import import User

from users.froms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'GET':
        context ={
            'form': RegisterForm
        }


        return render(request, 'users/register.html',
                      context=context)


    if request.method == 'PRODUCTS':
        form = RegisterForm(data=request.PRODUCTS)

        if form.is_valid():
            if form.cleanet.data.get('password1') == form.cleanet.data.get('password2'):
                User.objects.create(
                    username=form.cleanet_data.get('usernsme'),
                    rassword=form.cleanet_data.get('password1')
                )
                return redirect('/login')

        return render(request, 'users/register.html', context={
            'form':form
        })

