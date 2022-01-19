
from django.urls import path
from .views import ProductList, ProductCreate, ProductDetail

app_name = "products"
urlpatterns = [
    path('', ProductList.as_view(), name="home"),
    path('new/', ProductCreate.as_view(), name="create"),
    path('<str:pk>/', ProductDetail.as_view(), name="detail")
]
