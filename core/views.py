from django.shortcuts import render,HttpResponse

from .models import  Contact

# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html',context)

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        msg=request.POST.get('msg')
        subject=request.POST.get('subject')
        ct = Contact()
        ct.name=name
        ct.email=email
        ct.contact=contact
        ct.message=msg
        ct.subject=subject
        ct.save()
        return render(request, 'core/contact.html')
        # return HttpResponse("<h1> Successs  : "+str(t)+"<h1>")
    else:
        context = {'contact': 'active'}
        return render(request, 'core/contact.html',context)
