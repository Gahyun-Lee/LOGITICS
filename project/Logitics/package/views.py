from django.shortcuts import render, redirect
from .models import Packages
from hub.models import Hubs

# Create your views here.
def index(request):
    num = request.session.get('user')

    hubs = Hubs.objects.all()
    
    queue = list()
    
    if num == 'manager19':
        packages = Packages.objects.all()
    
    elif num == None:
        return redirect(login)
    
    else:
        packages = Packages.objects.filter(id=num)
    
    for package in packages:
        for hub in hubs:
            print(hub.que)
            if hub.que == None:
                queue.append(['',''])
                break
            que = hub.que.split('-')
            for q in que:
                if package.id == int(q):
                    queue.append([package.id, hub.name, hub.dest])
    
    return render(request, 'package/index.html', {'packages': packages, 'queue': queue})

def login(request):
    if request.method == 'GET':
        return render(request, 'package/login.html')
    
    else:
        num = int(request.POST.get('num'))
        name = request.POST.get('name')
        
        if num==00000 and name=='manager19':
            request.session['user'] = name
            return redirect(index)
        
        else:
            package = Packages.objects.filter(id=num, name=name)

            if package:
                request.session['user'] = num
                return redirect(index)
            
        return redirect(login)
    
def logout(request):
    del(request.session['user'])
    return redirect(login)