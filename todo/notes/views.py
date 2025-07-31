from django.shortcuts import render, redirect, HttpResponse
from notes.models import test
# Create your views here.

def todo(request):
    
    data = test.objects.all() ## Getting all the data from table to django
    
    # dict_one = {
    #     'data':data,      ## It is an option
    # }
    
    
    if(request.method == 'POST'):
        var1 = request.POST.get('title')
        var2 = request.POST.get('task')
        
        test_instance = test(title=var1, task=var2) ## Creating a new entry as object
        test_instance.save()
        
        return redirect('todo')

    return render(request, 'todo.html',{'data':data})


def edit(request,id):
    data = test.objects.get(id=id)
    if(request.method == 'POST'):
        var1 = request.POST.get('title')
        var2 = request.POST.get('task')
        
        data.title = var1
        data.task = var2
        data.save()       
        
        return redirect('todo')

    return render(request, 'edit.html',{'data':data})
    
    

def delete(request,id):
    data = test.objects.get(id=id)
    data.delete()
    
    return redirect('todo')

