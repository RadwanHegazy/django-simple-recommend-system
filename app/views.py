from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from .models import Video


@login_required
def home (request) :
    return render(request,'home.html')

@login_required
def upload (requset) :

    contx = {}

    if requset.method == 'POST' :
        video = requset.FILES['video']

        user = requset.user
        genres = str(requset.POST['genres']).split('@')
        genres = ' '.join(genres)

        Video.objects.create(
            user = user,
            video = video,
            genre = genres,
        )

        contx['msg'] = 'تم رفع الفيديو بنجاح'
        

    return render(requset,'upload.html',contx)


def login (request) :

    if request.method == "POST" :
        email = request.POST['email']
        password = request.POST['password']
        
        try :
            getUser = User.objects.get( email = email )
            auth = authenticate(username=getUser.username,password=password)
        
            if auth != None :
                auth_login(request,user=getUser)
                return redirect('home')

            
        except Exception as error:
            pass            

    return render(request,'login.html')


def register (request) : 
    
    if request.method == "POST" :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username = username).exists() == False :
            u = User.objects.create(
                username = username,
                email = email,
            )
            
            u.set_password(password)
            u.save()

            auth_login(request,user=User.objects.get(username=username))
            
            return redirect('home')


        
    return render(request,'register.html')
    