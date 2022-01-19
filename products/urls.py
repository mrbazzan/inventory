
from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path('', views.ProductList.as_view(), name="home"),
    path('new/', views.ProductCreate.as_view(), name="create"),
    path('<str:pk>/', views.ProductDetail.as_view(), name="detail"),
    path('<str:pk>/edit/', views.ProductEdit.as_view(), name="edit"),
    path('<str:pk>/delete/', views.ProductDelete.as_view(), name="delete"),
]
