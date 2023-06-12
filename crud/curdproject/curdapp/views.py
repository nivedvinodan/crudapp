from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from .models import Task
# Create your views here.
def crud(request):
    return render(request,'crud.html')
def crud(request):
    # return HttpResponse("hello")
    obj = Task.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        name=request.POST.get('name','')
        desc = request.POST.get('desc','')
        task=Task(slno=slno,name=name,desc=desc)
        task.save()

    return render(request,'crud.html',{'task1':obj})


def Delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def Update(request, task_id1):
    task = get_object_or_404(Task, id=task_id1)
    if request.method == 'POST':
        task.slno = request.POST.get('slno')
        task.item_name = request.POST.get('item_name')
        task.desc = request.POST.get('desc')

        task.save()
        return redirect('/')
        # task=task.objects.all()
    return render(request, 'update.html', {'task': task})