
from django.shortcuts import redirect
from django.views.generic import FormView, ListView

from order.forms import OrderForm
from order.models import Order

class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    # form 생성시 어떤 인자값을 전달할지 결정
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

# 주문정보 조회
class OrderList(ListView):
    model = Order
    template_name = 'order/order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            fcuser__username=self.request.user)
        return queryset