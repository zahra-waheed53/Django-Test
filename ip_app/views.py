from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Product, Logs
from .forms import ProductForm
from .log import log_create

def Home(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        user_ip = user_ip.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(f'Hello world <br> You are visiting from: {user_ip}')

def ProductDetail(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    return render(request, 'ip_app/product_details.html', {'product':product})

def Addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            log_create('CREATED', 'Product', product.id, f'New product created: Id:{product.id} Name: {product.name}')
            return redirect('product_details', product_id = product.id)
    else:
        form = ProductForm()

    return render(request, 'ip_app/add_product.html',{'form':form} )



def UpdateProduct(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            old_name = product.name
            updated_name = form.save()
            log_create('UPDATED', 'Product', updated_name.id, f'Updated product: Id:{updated_name.id} Old name: {old_name} New Name: {updated_name.name}')
            return redirect('product_details', product_id = updated_name.id)
    else:
        form = ProductForm()
    return render(request, 'ip_app/add_product.html', {'form':form})


def DeleteProduct(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    if request.method == 'POST':
        product_name = product.name
        productid = product.id
        product.delete()
        log_create('DELETED', 'Product', productid, f'Deleted Product: Id: {productid} Name: {product_name}')
        return redirect('log_list')
    return render(request, 'ip_app/delete.html', { 'product':product})


def LogsList(request):
    logs = Logs.objects.all().order_by('-action_time')
    return render(request, 'ip_app/logs.html', {'logs':logs})