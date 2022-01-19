
from django.urls import path
from .views import ProductList, ProductCreate

app_name = "products"
urlpatterns = [
    path('', ProductList.as_view(), name="home"),
    path('new/', ProductCreate.as_view(), name="create"),
]
