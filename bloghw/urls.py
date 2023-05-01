
from django.contrib import admin
from django.urls import path
from bloghw import settings
from Products.views import main_page_view, products_view, product_detail_view, product_create_view
from django.conf.urls.static import static


from bloghw import settings
from produts.views import (
    main_page_view,
    products_view,
    products_detail_view,
    products_create_view
)
from users.forms import register_view, auth_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', main_view),
    # path('hello/', hello_view),
    # path('now_date/', now_date_view),
    # path('goodbye/', goodbye_view),
    path('', main_view),
    path('products/', products_view),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', products_view()),

    path('users/register/, register_view'),
    path('users/login/', auth_view)
    path('users/logout', logout_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)