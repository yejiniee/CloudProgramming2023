from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from order.forms import OrderForm
from .models import Product, ProductCategory
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from users.decorators import admin_required


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product_list = Product.objects.filter(name__contains=searched)
        return render(request, 'product/product_list.html', {'searched': searched, 'product_list': product_list})
    else:
        return render(request, 'product/product_list.html', {})

#@method_decorator(admin_required, name = 'dispatch')
class ProductRegister(FormView):
    template_name = 'product/product_register.html'
    form_class = RegisterForm
    success_url = '/'

'''
    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            stock=form.data.get('stock'),
            description=form.data.get('description')
        )
        product.save()
        return super().form_valid(form)
'''
'''
    def get_context_data(self, **kwargs):
        context = super(ProductRegister, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        context['no_category_post_count'] = Product.objects.filter(category=None).count()
        return context
'''

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