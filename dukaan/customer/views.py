from django.shortcuts import render, redirect, HttpResponse
from customer.models import customer

# Create your views here.
def customer_details(request):
    data = customer.objects.all()

    if request.method == 'POST':
        name = request.POST.get('c_name')
        number = int(request.POST.get('c_number'))
        address = request.POST.get('c_address')             
               

        customer_instance = customer(
            c_name = name,
            c_contact = number,
            c_address = address,
        )
        customer_instance.save()

        return redirect('customer')

    return render(request, 'customer.html', {'customers': data})

