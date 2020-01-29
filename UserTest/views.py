from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,LoginForm
from .models import Register
import matplotlib.pyplot as plot
from django.views.generic import CreateView
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, "index1.html")


def myName(request):
	return HttpResponse(" Hello Namatullah Wahidi")

def Graph(request):
    dic={'name':'namatullah','last_name':'Wahidi','job':'student'}
    return render(request, "main.html",{'data': dic})
def News(request):
    return  render(request,"news.html")
def Bootstrap(request):
    return render(request, "base.html")
def RegisterView(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        newUser=Register()
        newUser.name=form.cleaned_data.get('name')
        newUser.email=form.cleaned_data.get('email')
        newUser.password=form.cleaned_data.get('password')
        newUser.agree=form.cleaned_data.get('agree')

        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        newUser.image=fs.url(name)

        messages.info(request,"Successfully Registered")
        newUser.save()
        context={'newUser':newUser,'url':fs.url(name)}
        print(" for is valid ok")
        return render(request, 'index1.html', context)

    context = {
        "form": form
    }
    print("form is invalid")
    return render(request, 'users/register.html', context)

def Login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        #UserTest=Register(email=email,password=password)
        user=Register.objects.filter(email=email,password=password).values()
        for share in user:
            print(share['name'])
        if(not user):
            messages.info(request, "Email or password is invalid")
            return render(request, 'users/login.html', context)
        else:
            messages.success(request,"Successfully inserted")
            user1=""
            fs=FileSystemStorage()
            for u in user:
                user1=u
                # imageName=fs.save()
            context = {'newUser': user1}
            return render(request, 'users/templates/index1.html', context)
    return render(request, "users/login.html", context)


def Logout(request):
    messages.success(request, "Başarıyla Çıkış Yaptınız")
    return redirect("index1")


def uploadFile(request):
    context={}
    if request.method=="POST":
        upload_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(upload_file.name,upload_file)
        context['url']=fs.url(name)
    return render(request,'users/upload.html',context)

