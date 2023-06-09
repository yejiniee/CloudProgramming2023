from django.shortcuts import render
from product.models import Product

def main(request):
    product_list = Product.objects.order_by('-pk')[:]
    return render(request, 'shop/main.html',
                  {
                      'product_list' : product_list,
                  }
                  )