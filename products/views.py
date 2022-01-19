from django.http import HttpResponseRedirect, HttpResponse
from .models import Product
from django.views import generic
from django.urls import reverse_lazy

import csv
# Create your views here.


class ProductList(generic.ListView):
    model = Product
    ordering = 'id'
    paginate_by = 5
    template_name = 'products/home.html'


class ProductCreate(generic.CreateView):
    model = Product
    template_name = "products/new.html"
    success_url = reverse_lazy('products:home')
    fields = ['name', 'description', 'location', 'driver']

    def get_context_data(self, **kwargs):
        kwargs["type"] = "Create"
        return super().get_context_data(**kwargs)


class ProductDetail(generic.DetailView):
    template_name = "products/detail.html"
    queryset = Product.objects.all()


class ProductEdit(generic.UpdateView):
    queryset = Product.objects.all()
    template_name = "products/new.html"
    fields = ['name', 'description', 'location']

    def get_success_url(self):
        return reverse_lazy('products:detail', args=(self.kwargs["pk"],))

    def get_context_data(self, **kwargs):
        kwargs["type"] = "Edit"
        return super().get_context_data(**kwargs)


class ProductDelete(generic.DeleteView):
    model = Product
    success_url = reverse_lazy("products:home")
    template_name = "products/delete.html"


def generate_csv_view(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={'Content-Disposition': 'attachment;filename="products.csv"'},
    )

    if not Product.objects.all():
        return HttpResponse("No inventory data.")

    writer = csv.writer(response)
    for data in Product.objects.all():
        writer.writerow([data.id, data.description, data.location, data.driver.username])

    return response
