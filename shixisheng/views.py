from django.shortcuts import render_to_response,redirect
from django.core.context_processors import csrf
from .models import  Sms

def home(request):
    c = {}
    c.update(csrf(request))
    # ... view code here
    all_sms = Sms.objects.all().order_by("-id")
    c["all_sms"] = all_sms

    return render_to_response("index.html", c)



def new(request):
        if request.method == "POST":
                a = Sms()
                a.name    = request.POST['name']
                a.phone   = request.POST['phone']
                a.content = request.POST['content']
                a.save()
        return redirect ("/")
def d(request,id):
        a = Sms.objects.get(id = int(id))
        a.delete()
        return redirect ("/")

def display(request,id):
        a = Sms.objects.get(id = int(id))
	d={"a":a}
        return render_to_response("display.html",d)
