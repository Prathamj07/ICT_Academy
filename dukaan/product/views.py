from django.shortcuts import render, redirect
from product.models import Item

def item_view(request):
    data = Item.objects.all()

    if request.method == 'POST':
        name = request.POST.get('p_name')                    
        quantity = int(request.POST.get('p_quantity'))       
        price = int(request.POST.get('p_price'))              
        discount = int(request.POST.get('p_discount'))        

        item_instance = Item(
            p_name=name,
            p_quantity=quantity,
            p_price=price,
            p_discount=discount
        )
        item_instance.save()

        return redirect('product')

    return render(request, 'products.html', {'itemss': data})

