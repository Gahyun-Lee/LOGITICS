from django.shortcuts import render, redirect
from .models import Hubs

# Create your views here.
def hubs(request):
    if request.method == 'GET':
        hubs = Hubs.objects.all()
        return render(request, 'hub/hubs.html', {'hubs': hubs})

    else:
        name = request.POST['name']
        dest = request.POST['dest']
        weight = request.POST['weight']
        
        if not Hubs.objects.filter(name=name, dest=dest):
            hub = Hubs()
            hub.name = name
            hub.dest = dest
            hub.weight = weight
            hub.save()
            
        return redirect('hubs')
    
def more(request, id):
    if request.method == 'GET':
        hub = Hubs.objects.get(id=id)
        que = hub.que.split('-')
        return render(request, 'hub/more.html', {'hub': hub, 'que': que})
    
    else:
        hub = Hubs.objects.get(id=id)
        hub.weight = request.POST['weight']
        hub.save()
        return redirect('more', id)
    
def delete(request, id):
    hub = Hubs.objects.get(id=id)
    hub.delete()
    return redirect('hubs')