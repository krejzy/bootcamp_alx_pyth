from django.shortcuts import render, HttpResponse

# Create your views here.
from products.model

def hello_world_name


def products_list(request):
    products = Product.objct.all()
    output = ""
    for prod in products:
        output += f'(prod.id)  <a href="/products/(prod.id">(prod.name)</a><hr>'
        return HttpResponse(output)

    def products_list(request):
        product = Product.objects.all()
        return render(
            request = request
            context =('product')

        )