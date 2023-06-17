from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from order.forms import OrderForm
from .models import Product, ProductCategory
from .forms import RegisterForm
from django.views.generic.edit import FormView


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product_list = Product.objects.filter(name__contains=searched)
        return render(request, 'product/product_list.html', {'searched': searched, 'product_list': product_list})
    else:
        return render(request, 'product/product_list.html', {})

class ProductRegister(FormView):
    template_name = 'product/product_register.html'
    form_class = RegisterForm
    success_url = '/'


class ProductList(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'product_list'



class ProductDetail(DetailView):
    template_name = "product/product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('/')