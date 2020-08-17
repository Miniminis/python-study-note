from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.utils.decorators import method_decorator

from .models import FcMallProduct
from .forms import ProductCreateForm

from order.forms import OrderCreateForm
from user.decorators import admin_required

from rest_framework import generics, mixins
from .serializers import ProductSerializer

class ProductListViewApi(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return FcMallProduct.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailViewApi(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return FcMallProduct.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Create your views here.
class ProductListView(ListView):
    model = FcMallProduct
    template_name = 'product.html'
    context_object_name = 'product_list'

class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = FcMallProduct.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = OrderCreateForm(self.request)
        return ctx

@method_decorator(admin_required, name='dispatch')
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

