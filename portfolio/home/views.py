from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    context={'name':'Harshada', 'profession':'Engineer'}
    return render(request,'home.html',context)
def about(request):
    # return HttpResponse("This is about Harshada")
    return render(request,'about.html')
def projects(request):
    # return HttpResponse("This is Harshada's Project")
    return render(request,'projects.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ins = Contact(name=name,email=email,message=message)
        ins.save()
        
    # return HttpResponse("contact Harshada")
    return render(request,'contact.html')
