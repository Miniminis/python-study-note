from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import FormView, ListView

from .forms import OrderCreateForm
from .models import FcMallOrder
from user.decorators import login_required
from user.models import FcUser
from product.models import FcMallProduct

# Create your views here.
@method_decorator(login_required, name='dispatch')
class OrderCreateView(FormView):
    form_class = OrderCreateForm
    success_url = '/product/'

    def form_valid(self, form):
        prod = FcMallProduct.objects.get(pk=form.data.get('product'))
        order = FcMallOrder(
            quantity=form.data.get('quantity'),
            product=prod,
            fcuser=FcUser.objects.get(email=self.request.session.get('user'))
        )
        order.save()
        prod.stuck -= int(form.data.get('quantity'))
        prod.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))
    
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request' : self.request
        })
        return kw

@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    template_name = 'orders.html'
    context_object_name = 'order_list'
    queryset = FcMallOrder.objects.all()


