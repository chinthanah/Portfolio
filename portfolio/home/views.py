from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')
def About(request):
    return render(request,'about.html')
def Projects(request):
    return render(request,'projects.html')
def Contact(request):
    if request.method=="POST":
        print("posted successfully")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        textarea=request.POST['textarea']
        print(name,email,phone,textarea)
        ins=Contact(name=name,email=email,phone=phone,textarea=textarea)
        ins.save()
    return render(request,'contact.html')       