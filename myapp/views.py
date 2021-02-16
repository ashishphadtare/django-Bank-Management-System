from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from myapp.database import Operation
import datetime
# Create your views here.

x=datetime.date.today()

def login(request):
    return render(request,"Login.html")

def register(request):
    return render(request,"Register.html")

def dash(request):
    return render(request,"dashboard.html",{"time":x})

def forg(request):
    return render(request,"forgotpas.html")

def forgotpas(request):
    nm=request.POST['user']
    ps=request.POST['pas']
    cps=request.POST['cpas']
    obj=Operation('localhost','root','','bank')
    data=obj.forgotpassword(nm,ps)
    if(ps==cps):
        return render(request,"login.html")
    else:
        return render(request,"forgotpas.html",{"msg":"please fill same password"})


def check_login(request):
    obj=Operation('localhost','root','','bank')
    if request.method=='POST':
        nm=request.POST['email']
        ps=request.POST['password']
        data=obj.Checklogin(nm,ps)
        # print(data)
        if(len(data)==0):
            return render(request,"login.html",{"msg":"Invalid Username and Password."})
        else:
            request.session['name']=nm

            request.session['reg_id']=data[0][8]

            return render(request,"dashboard.html",{"u_name":request.session['name'],"time":x})


    


@api_view(['GET','POST'])
def addreg(request):
    obj=Operation('localhost','root','','bank')
    if request.method=='POST':
        fname=request.POST['full_name']
        email=request.POST['email_address']
        uname=request.POST['username']
        phn=request.POST['phn_no']
        pan=request.POST['pan']
        address=request.POST['permanent_address']
        adhar=request.POST['adharnumber']
        pas=request.POST['pas']
        data=obj.AddRegister(fname,email,uname,phn,pan,address,adhar,pas)
        return render(request,"Register.html",{"msg":data})

@api_view(['GET','POST'])
def balnc(request):
    obj=Operation('localhost','root','','bank')
    rid=request.session["reg_id"]
    data=obj.GetBalance(rid)
    return JsonResponse(data,safe=False)

@api_view(['GET','POST'])
def amtadd(request):
    obj=Operation('localhost','root','','bank')
    rid=request.session["reg_id"]
    bal=request.POST['amt']
    data=obj.GetBalance(rid)
    calculate=int(data[0][3])+int(bal)
    data2=obj.Addmoney(rid,str(calculate))
    return render(request,"dashboard.html",{"u_name":request.session['name'],"time":x})


@api_view(['GET','POST'])
def withdraw(request):
    obj=Operation('localhost','root','','bank')
    rid=request.session["reg_id"]
    bal=request.POST['amt']
    data=obj.GetBalance(rid)
    bbal=data[0][3]
    if(int(bbal)<int(bal)):
        return render(request,"dashboard.html",{"u_name":request.session['name'],"msg2":"You have not sufficiend balance"})
    else:
        calculate=int(bbal)-int(bal)
        data2=obj.Addmoney(rid,str(calculate))
    return render(request,"dashboard.html",{"u_name":request.session['name'],"time":x})

@api_view(['GET','POST'])
def sendmoney(request):
    obj=Operation('localhost','root','','bank')
    rid=request.session["reg_id"]
    bal=request.POST['amt']
    ac=request.POST['acc']
    data=obj.GetBalance(rid)
    bbal=data[0][3]
    calculate=int(bbal)-int(bal)
    data2=obj.Addmoney(rid,str(calculate))
    data5=obj.SendMoney(ac,bal)
    return render(request,"dashboard.html",{"u_name":request.session['name'],"time":x})













