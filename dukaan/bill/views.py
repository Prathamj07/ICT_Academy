from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, redirect
from customer.models import customer
from product.models import Item
from .models import bill, billItem
# Create your views here.
def create_bill(request):
    if (request.method== 'POST'):
        c_id = request.POST.get('customer_id')
        p_ids = request.POST.getlist('product_ids')
        i_quantity = request.POST.getlist('quantities')
        
        customer_instance = customer.objects.get(id = c_id)
        bill_instance= bill.objects.create(customer = customer_instance)
        
        
        for pid, qty in zip(p_ids, i_quantity):
            if qty:
                product = Item.objects.get(id=pid)
                billItem.objects.create(
                    bill=bill_instance,
                    product=product,
                    quantity=int(qty)
                )
             
                
                
        return redirect('show_bill', bill_id= bill_instance.id)
    
    customers = customer.objects.all()
    products = Item.objects.all()
    bills = bill.objects.all()

    return render(request, 'bill.html', {
        'customers': customers,
        'items': products,
        'bills':bills
    })
    


def total_bill(request, bill_id):
    bill_instance = bill.objects.get(id=bill_id)
    items = billItem.objects.filter(bill=bill_instance)
    
    total =0
    for item in items:
        price = item.product.p_price
        discount = item.product.p_discount
        quantity = item.quantity
        
        dis = price - (price*discount/100)
        total += dis * quantity
    bill_instance.total_amount = total
    bill_instance.save()
    
    return render(request, 'show_bill.html', {
        'bill': bill_instance,
        'items': items,
        'total': total
    })
    

        
    
    
    