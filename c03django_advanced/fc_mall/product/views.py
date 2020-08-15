from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import FcMallProduct
from .forms import ProductCreateForm

# Create your views here.
class ProductListView(ListView):
    model = FcMallProduct
    template_name = 'product.html'
    context_object_name = 'product_list'

class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = FcMallProduct.objects.all()
    context_object_name = 'product'

class ProductCreateView(FormView):
    template_name = 'product_create.html'
    form_class = ProductCreateForm
    success_url = '/product/'

    def form_valid(self, form):
        product = FcMallProduct(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stuck=form.data.get('stuck')
        )
        product.save()

        return super().form_valid(form)

