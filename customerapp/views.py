from django.shortcuts import render,redirect
from crmapp.models import Customer
from django.views.decorators.cache import cache_control
import datetime
from . models import Response


# Create your views here.
@cache_control(no_cache=True, must_revalidation=True, no_store=True)
def customerhome(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            cust=Customer.objects.get(emailaddress=userid)
            return render(request,"customerhome.html",locals())
    except KeyError:
        return redirect("crmapp:login")
def logout(request):
    try:
        del request.session["userid"]
    except KeyError:
        return redirect('crmapp:login')
    return redirect("crmapp:login")
@cache_control(no_cache=True, must_revalidation=True, no_store=True)
def response(request):
    try:
        cust=Customer.objects.get(emailaddress=request.session['userid'])
        if request.session ['userid']!=None:
            if request.method=="POST":
                name=cust.name
                contactno=cust.contactno
                emailaddress=cust.emailaddress
                responsetype=request.POST['responsetype']
                subject=request.POST['subject']
                responsetext=request.POST['responsetext']
                posteddate=datetime.datetime.today()
                res=Response(name=name, contactno=contactno, emailaddress=emailaddress,  responsetype=responsetype, subject=subject, responsetext=responsetext, posteddate=posteddate)
                res.save()
                msg="Your response has been send successfuly"
                return render(request, "response.html",{'msg':msg})
        return render(request,"response.html")
    except KeyError:
        return redirect("crmapp:login") 

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewprofile(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            cust=Customer.objects.get(emailaddress=userid)
            if request.method=="POST":
                name=request.POST["name"]
                gender=request.POST["gender"]
                address=request.POST["address"]
                contactno=request.POST["contactno"]
                emailaddress=request.POST["emailaddress"]
                Customer.objects.filter(emailaddress=emailaddress).update(name=name,gender=gender,address=address,contactno=contactno)
                return redirect("customerapp:customerhome")
            return render(request,"viewprofile.html",locals())
    except KeyError:
        return redirect("crmapp:login")