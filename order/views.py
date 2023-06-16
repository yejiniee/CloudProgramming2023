from django.db import transaction
from django.shortcuts import redirect
from django.views.generic import FormView

from order.forms import OrderForm
from order.models import Order
from product.models import Product
from users.decorators import login_required
from users.models import Users


#@method_decorator(login_required, name = 'dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/'
    '''
    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity = form.data.get('quantity'),
                product = prod,
                user = Users.objects.get(email = self.request.session.get('user'))
            )
            order.save()

            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        return super().form_valid(form)
    '''
    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    # form을 생성할 때 어떤 인자값을 전달해서 만들건지를 결정하는 함수
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw