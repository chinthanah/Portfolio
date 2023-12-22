from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')
def About(request):
    return render(request,'about.html')
def Projects(request):
    return render(request,'projects.html')
def contact_view(request):
    if request.method=="POST":
        print("posted successfully")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        print("data has been written")
    return render(request,'contact.html')       