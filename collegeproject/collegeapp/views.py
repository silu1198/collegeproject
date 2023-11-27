from django.shortcuts import redirect, render
from collegeapp.models import reg
# Create your views here.
def display(request):
    return render(request,'college1.html')
def doc1(request):
    if request.method=='POST':
        obj=reg()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.age=request.POST.get('age')
        obj.save()
        return redirect('status')
    return render(request,'college1.html')
def status(request):
    obj=reg.objects.all()
    return render(request,'table.html',{'data':obj})
def update(request,pk):
    obj=reg.objects.get(id=pk)
    if request.method=='POST':
        obj=reg.objects.get(id=pk)
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.age=request.POST.get('age')
        obj.save()
        return redirect('status')
    return render(request,'update.html',{'data':obj})    
def delete(request,pk):
    obj=reg.objects.get(id=pk)
    obj.delete()
    return status(request)