from django.shortcuts import render, HttpResponse, redirect
from test_app.models import test

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dev(request):
    return render(request, 'dev.html')

def contact(request):
    
    data = test.objects.all() ## Getting all the data from table to django
    
    # dict_one = {
    #     'data':data,      ## It is an option
    # }
    
    
    if(request.method == 'POST'):
        var1 = request.POST.get('name')
        var2 = request.POST.get('number')
        
        test_instance = test(name=var1, number=var2)
        test_instance.save()
        
        return redirect('contact')
       
        
        
        
    # return render(request, 'contact.html')
    return render(request, 'contact.html',{'data':data})


