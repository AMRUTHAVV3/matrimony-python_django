from django.shortcuts import render,redirect
from userapp.models import userregistrationdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from userapp.models import customer_registrationdb,sendmessagedb,feedbackdb



# Create your views here.
def home_fn(req):
    return render(req,'home.html')
def login2_fn(req):
    return render(req,'login2.html')

def saveregistration_fn(req):
    if req.method == 'POST':
        un=req.POST.get('username')
        uiml=req.POST.get('email')
        pas=req.POST.get('pass')
        mob=req.POST.get('number')
        obj=userregistrationdb(uname=un,uemail=uiml,upass=pas,mobile=mob)
        obj.save()
        return redirect(login2_fn)

def signup_fn(req):
    if req.method=='POST':
        u_name=req.POST.get('uname')
        pwd=req.POST.get('upass')
        if userregistrationdb.objects.filter(uname=u_name,upass=pwd).exists():
            messages.success(req,'user login succesfully')
            req.session['username'] = u_name
            req.session['password'] = pwd
            return redirect(home_fn)
        else:
            messages.error(req, 'invalid user')
            return redirect(login2_fn)
    return redirect(home_fn)

def userlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(home_fn)

def main_fn(req):
    return render(req,'main.html')

def registration_fn(req):
    return render(req,'registration.html')
def saveregister_fn(req):
    if req.method=='POST':
        fn = req.POST.get('first_name')
        ln = req.POST.get('last_name')
        gn = req.POST.get('gender')
        db = req.POST.get('dob')
        pic = req.FILES['image']

        cst = req.POST.get('caste')
        con = req.POST.get('number')
        eml = req.POST.get('email')
        city = req.POST.get('city')
        quali = req.POST.get('quali')
        wds = req.POST.get('Workaddress')
        hby = req.POST.get('Hobby')
        oc = req.POST.get('OOCUPATION')
        ffn = req.POST.get('fname')
        mn = req.POST.get('mname')
        fcon = req.POST.get('fnumber')
        fads = req.POST.get('address')

        # strn = req.POST.get('street')
        # zp = req.POST.get('zip')
        # srt = req.POST.get('place')
        cntry = req.POST.get('country')
        uname = req.POST.get('username')
        pasw = req.POST.get('password')
        obj =customer_registrationdb(fname=fn,lname=ln,gender=gn,dob=db,picture=pic,caste=cst,contact=con,email=eml,city=city,qualification=quali,workaddress=wds,occupation=oc,hobby=hby,fathername=ffn,mothername=mn,fathercontact=fcon,address=fads,country=cntry,username=uname,password=pasw)
        obj.save()

        return redirect(home_fn)

def user_login(req):
    if req.method=='POST':
        u_name=req.POST.get('uname')
        pwd=req.POST.get('upass')
        if customer_registrationdb.objects.filter(username=u_name,password=pwd).exists():
            messages.success(req,'user login succesfully')
            req.session['username'] = u_name
            req.session['password'] = pwd
            return redirect(home_fn)
        else:
            messages.error(req, 'invalid user')
            return redirect(registration_fn)
    return redirect(registration_fn)


def gallery_fn(req):
    fdata=customer_registrationdb.objects.all().filter(gender="female")

    context = {
        'fdata': fdata,

    }
    return render(req,'gallery.html',context)


# def displayallcustomer_fn(req):
#
#     data=customer_registrationdb.objects.all()
#     return render(req,'displaygallery.html',{'data':data})
#
# def deletecustomer_fn(req,dataid):
#     data=customer_registrationdb.objects.filter(id=dataid)
#     data.delete()
#     return redirect(displayallcustomer_fn)
def malegallery_fn(req):
    data=customer_registrationdb.objects.all().filter(gender="male")
    context={
        'data':data,

    }

    return render(req,'malegallery.html',context)

def viewprofile_fn(req,dataid):
    profile=customer_registrationdb.objects.get(id=dataid)
    context={
        'profile':profile
    }
    return render(req,'view profile.html',context)

def savemessage_fn(req):

    if req.method=='POST':
        un=req.POST.get('username')


        fn=req.POST.get('fname')
        ln=req.POST.get('lname')
        msg=req.POST.get('message')
        obj=sendmessagedb(user_name=un,message=msg,fname=fn,lname=ln)
        obj.save()

        return redirect(gallery_fn)


def sendmessage_fn(req):
    msgs=sendmessagedb.objects.filter(user_name=req.session['username'])
    # data=sendmessagedb.objects.all()
    return render(req,"sendmessage.html",{'msgs':msgs})

def deletemessage(req,dataid):
    data = sendmessagedb.objects.filter(id=dataid)
    data.delete()
    return redirect(sendmessage_fn)

def displayuser_details(req):
    p=customer_registrationdb.objects.filter(username=req.session['username'])


    return render(req,'displayUser.html',{'p':p})

def updateuser_details(req,dataid):
    if req.method=='POST':
        ln = req.POST.get('first_name')


        lln = req.POST.get('last_name')
        gen = req.POST.get('gender')
        ldob = req.POST.get('dob')

        lcst = req.POST.get('caste')
        lnum = req.POST.get('number')
        leml = req.POST.get('email')
        lcity = req.POST.get('city')
        lquali = req.POST.get('quali')
        lworkads = req.POST.get('Workaddress')
        lhobby = req.POST.get('Hobby')
        loccu = req.POST.get('OOCUPATION')

        lfn = req.POST.get('fname')
        lmn = req.POST.get('mname')
        lfnum = req.POST.get('fnumber')
        ladrs = req.POST.get('address')
        lcntry = req.POST.get('country')
        luser = req.POST.get('username')
        lpass = req.POST.get('password')
        try:
            lpic = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(lpic.name, lpic)
        except MultiValueDictKeyError:
            file = customer_registrationdb.objects.get(id=dataid).picture
        customer_registrationdb.objects.filter(id=dataid).update(fname=ln,lname=lln,gender=gen,dob=ldob,caste=lcst,contact=lnum,email=leml,city=lcity,qualification=lquali,occupation=loccu,workaddress=lworkads,hobby=lhobby,fathername=lfn,mothername=lmn,fathercontact=lfnum,address=ladrs,country=lcntry,username=luser,password=lpass,picture=file)
        return redirect(home_fn)


def general_info(req,dataid):
    profile=customer_registrationdb.objects.get(id=dataid)
    context= {
        'profile': profile
    }
    return render(req,'generalinfo.html',context)
def familydetail_fn(req,dataid):
    profile=customer_registrationdb.objects.get(id=dataid)
    context= {
        'profile': profile
    }
    return render(req,'familydetails.html',context)

def educationdetail_fn(req,dataid):
    profile=customer_registrationdb.objects.get(id=dataid)
    context= {
        'profile': profile
    }
    return render(req,'education.html',context)

def text_msg_fn(req,dataid):
    profile=customer_registrationdb.objects.get(id=dataid)
    context={
        'profile': profile
    }
    return render(req,'text_msg.html',context)

def savetext_msg(req):
    if req.method=='POST':
        un=req.POST.get('username')


        fn=req.POST.get('fname')
        ln=req.POST.get('lname')
        msg=req.POST.get('message')
        obj=sendmessagedb(user_name=un,message=msg,fname=fn,lname=ln)
        obj.save()

        return redirect(gallery_fn)

def requestedmsg_fn(request):
    receivemsg=sendmessagedb.objects.filter(user_name=request.session['username'])

    return render(request,'requestedmsg.html',{'receivemsg':receivemsg})


def text_feedback_fn(req):
    return render(req,'text_feedback.html')

def savefeedback_fn(req):
    if req.method=='POST':
        un=req.POST.get('username')
        fb=req.POST.get('feedback')
        obj=feedbackdb(user=un,feedback=fb)
        obj.save()
        return redirect(gallery_fn)

# def text_feedback(req,dataid):
#     profile=customer_registrationdb.objects.get(id=dataid)
#     context={
#         'profile': profile
#     }
#     return render(req,'text_feedback.html',context)
#
# def savefeedback_fn(req):
#     if req.method=='POST':
#         un=req.POST.get('username')
#         fn=req.POST.get('fname')
#         fdb=req.POST.get('feedback')
#         obj=sendmessagedb(user=un,fname=fn,feedback=fdb)
#         obj.save()
#
#         return redirect(gallery_fn)
