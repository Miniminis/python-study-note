from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from django.views.generic import FormView

# Create your views here.
class OrderCreateView(FormView):
    form_class = OrderCreateForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/', str(form.data.get('product')))
    
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request' : self.request
        })
        return kw

