from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        mobno=request.POST.get('mobno')
        email=request.POST.get('email')
        pwrd=request.POST.get('pword')
        reg=Register(uname=uname,mobno=mobno,email=email,pwrd=pwrd)
        reg.save()
        return redirect('index')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pwrd=request.POST.get('pwrd')
        user=Register.objects.get(uname=uname)
        if user.pwrd==pwrd:
            request.session['username']=uname
            data={'session':uname}
            return render(request,'home.html',context=data)
        else:
            data = {'status': "Incorrect Password!!!"}
            return render(request,'login.html',context=data)
    return render(request,'login.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return render(request,'index.html')

def libms(request):
    if request.method == 'POST':
        uname=request.session['username']
        fname=request.POST.get('fname')
        mobno=request.POST.get('mobno')
        email=request.POST.get('email')
        bokname=request.POST.get('bname')
        autname=request.POST.get('aname')
        bordt=request.POST.get('bokdt')
        retdt=request.POST.get('retdt')
        lib=Libms(uname=uname,fname=fname,mobno=mobno,email=email,bokname=bokname,autname=autname,bordt=bordt,retdt=retdt)
        lib.save()
        return redirect('home')
    return render(request,'libent.html')

def viewlib(request):
    if 'username' in request.session:
        d=Libms.objects.filter(uname=request.session['username'])
        data={'data':d}
        return render(request,'viewlib.html',context=data)