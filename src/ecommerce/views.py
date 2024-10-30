from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ProductModel
from django.views.decorators.http import require_POST

# List View
def product_model_list_view(request):
    queryset = ProductModel.objects.all()
    template = "ecommerce/list-view.html"  # Asegúrate de tener este template
    context = {"products": queryset}
    return render(request, template, context)

# Detail View
def product_model_detail_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    template = "ecommerce/detail-view.html"  # Crea este template
    context = {"product": product}
    return render(request, template, context)

# Create View
def product_model_create_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description', '')
        seller = request.POST.get('seller', '')
        color = request.POST.get('color', '')
        product_dimensions = request.POST.get('product_dimensions', '')

        product = ProductModel(
            title=title,
            price=price,
            description=description,
            seller=seller,
            color=color,
            product_dimensions=product_dimensions
        )
        product.save()
        return redirect('product-list')  # Asegúrate de tener este nombre en tu urls.py
    template = "ecommerce/create-view.html"  # Crea este template
    return render(request, template)

# Update View
def product_model_update_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    if request.method == "POST":
        product.title = request.POST.get('title', product.title)
        product.price = request.POST.get('price', product.price)
        product.description = request.POST.get('description', product.description)
        product.seller = request.POST.get('seller', product.seller)
        product.color = request.POST.get('color', product.color)
        product.product_dimensions = request.POST.get('product_dimensions', product.product_dimensions)
        product.save()
        return redirect('product-list')  # Asegúrate de tener este nombre en tu urls.py
    template = "ecommerce/update-view.html"  # Crea este template
    context = {'product': product}
    return render(request, template, context)

# Delete View
@require_POST
def product_model_delete_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    product.delete()
    return redirect('product-list')  # Asegúrate de tener este nombre en tu urls.py
