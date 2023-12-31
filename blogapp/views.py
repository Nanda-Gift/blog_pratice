from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from blogapp.models import blogconts
import re

# Create your views here.
def home(request):
    blogs = blogconts.objects.all()
    context={'blogs':blogs}
    return render(request,"home.html",context)

def know(request,id):
    blog = blogconts.objects.filter(Blog_Id=id)
    context={'blog': blog}
    return render(request,'know.html',context)



def register(request):
    flag=0
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
       
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return redirect('register') 
        if len(password)<=5:
            messages.warning(request,"Password must be atleast 5 character")
            return redirect('register') 
        elif not re.search("[a-z]", password):
            flag = -1
            
        elif not re.search("[A-Z]", password):
            flag = -1
            
        elif not re.search("[0-9]", password):
            flag = -1
            
        elif not re.search("[_@$#%^*()-]" , password):
            flag = -1  
        else:
            pass
        if(flag==0):
            try:
                if User.objects.get(username=email):
                    messages.info(request,"Email is Taken")
                    return redirect('register') 


            except Exception as identifier:
                pass
            user = User.objects.create_user(email,email,password)
            user.first_name=name
            user.is_active=True
            user.save()
            messages.success(request,"Account created")
            return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            auth.login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')

    return render(request, "login.html")

def logouts(request):
    logout(request)
    messages.success(request,"Logout success")
    return render(request,"login.html")

def create_blog(request):
    if request.method=="POST":              
                Blog_name=request.POST.get('Blog_name')
                photo_image=request.FILES.get('photo_image')
                Author_name=request.POST.get('Author_name')
                Blog_content=request.POST.get('Blog_content')
                stars=request.POST.get('stars')  
                created_by=request.POST.get('created_by')           

                query= blogconts(Blog_name=Blog_name,created_by=created_by,photo_image=photo_image,Author_name=Author_name,Blog_content=Blog_content,stars=stars)
                query.save()
                return redirect('/')

    return render(request,'create.html')

def blog_update(request,id):
    data=blogconts.objects.get(Blog_Id=id) 
    context={"data":data}

    if request.method=="POST":
        Blog_name=request.POST.get('Blog_name')
        photo_image=request.FILES.get('photo_image')
        Author_name=request.POST.get('Author_name')
        Blog_content=request.POST.get('Blog_content')
        stars=request.POST.get('stars')

        edit=blogconts.objects.get(Blog_Id=id)
        edit.Blog_name=Blog_name
        edit.photo_image=photo_image
        edit.Author_name=Author_name
        edit.Blog_content=Blog_content
        edit.stars=stars
        edit.save()
        messages.info(request,"Updates Successfully...")
        return redirect("/")
    
    return render(request,"update.html",context)

def delete(request,id):
    erase=blogconts.objects.get(Blog_Id=id)
    erase.delete()
    messages.info(request,"deleted successfully")
    return redirect('/')


def search(request):
    query=request.GET['search']
    if len(query)>100:
        allPosts=blogconts.objects.none()
    else:
        allPosts=blogconts.objects.filter(Blog_name__icontains=query)
    if allPosts.count()==0:
        messages.warning(request,"No Search Results")
    params={'allPosts':allPosts,'query':query}
    return render(request,"search.html",params)
        
