from django.urls import path
from api.views import *

urlpatterns = [
    path('categories/', category_list),
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/<int:category_id>/', category_detail)
]