
from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path('', views.ProductList.as_view(), name="home"),
    path('new/', views.ProductCreate.as_view(), name="create"),
    path('<int:pk>/', views.ProductDetail.as_view(), name="detail"),
    path('<int:pk>/edit/', views.ProductEdit.as_view(), name="edit"),
    path('<int:pk>/delete/', views.ProductDelete.as_view(), name="delete"),
    path('csv/', views.generate_csv_view, name="generate_csv"),
]
