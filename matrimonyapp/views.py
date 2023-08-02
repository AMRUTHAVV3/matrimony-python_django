from django.shortcuts import render,redirect
from matrimonyapp.models import customerdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from userapp.models import feedbackdb


# Create your views here.
def index_fn(req):
    return render(req,'index.html')
def addcustomer_fn(req):
    return render(req,'Addcustomer.html')
def savecustomer_fn(req):
    if req.method=='POST':
        cn = req.POST.get('cus_name')
        cpic = req.FILES['cus_pic']

        cnum = req.POST.get('cus_num')
        cmail = req.POST.get('cus_mail')
        cdob = req.POST.get('cus_dob')
        ccity = req.POST.get('cus_city')
        cads = req.POST.get('cus_ads')
        cfn = req.POST.get('cus_fname')
        cmn = req.POST.get('cus_mname')
        cpc = req.POST.get('cus_pcont')
        cwds = req.POST.get('cus_wadrs')
        ch = req.POST.get('cus_hob')
        cq=req.POST.get('cus_quali')
        co = req.POST.get('cus_occu')

        cc = req.POST.get('cus_cast')
        obj = customerdb(cname=cn,cpic=cpic,cno=cnum,emil=cmail,dob=cdob,city=ccity,adrs=cads,fname=cfn,mname=cmn,fcont=cpc,wadrs=cwds,hoby=ch,quali=cq,occutn=co,cast=cc)
        obj.save()

        return redirect(addcustomer_fn)
def displaycustomer_fn(req):

    data=customerdb.objects.all()
    return render(req,'Displaycustomer.html',{'data':data})

def editcustomer_fn(req,dataid):
    customer=customerdb.objects.get(id=dataid)
    return render(req,'editcustomer.html',{'customer':customer})

def updatecategory(req,dataid):
    if req.method=='POST':
        cn = req.POST.get('cus_name')


        cnum = req.POST.get('cus_num')
        cmail = req.POST.get('cus_mail')
        cdob = req.POST.get('cus_dob')
        ccity = req.POST.get('cus_city')
        cads = req.POST.get('cus_ads')
        cfn = req.POST.get('cus_fname')
        cmn = req.POST.get('cus_mname')
        cpc = req.POST.get('cus_pcont')
        cwds = req.POST.get('cus_wadrs')
        ch = req.POST.get('cus_hob')
        cq = req.POST.get('cus_quali')
        co = req.POST.get('cus_occu')

        cc = req.POST.get('cus_cast')
        try:
            cpic = req.FILES['cus_pic']
            fs = FileSystemStorage()
            file = fs.save(cpic.name, cpic)
        except MultiValueDictKeyError:
            file = customerdb.objects.get(id=dataid).cpic
        customerdb.objects.filter(id=dataid).update(cname=cn,cno=cnum,emil=cmail,dob=cdob,city=ccity,adrs=cads,fname=cfn,mname=cmn,fcont=cpc,wadrs=cwds,hoby=ch,quali=cq,occutn=co,cast=cc,cpic=file)
        return redirect(displaycustomer_fn)

def deletecustomer_fn(req,dataid):
    data=customerdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycustomer_fn)
def login_fn(req):
    return render(req,'login.html')

def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request,"login successfully")
                request.session['username'] = uname
                request.session['password'] = pwd
                return redirect(index_fn)
            else:
              messages.error(request,"invalid user")
              return redirect(login_fn)
        else:
            messages.error(request, "invalid user")
            return redirect(login_fn)
def admin_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(login_fn)

def viewfeedback_fn(req):
    data=feedbackdb.objects.all()
    return render(req,'viewfeedback.html',{'data':data})