from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customers,Session_model
from .forms import Customers_forms
import uuid
# Create your views here.
user1={}

def home(request):
    u=""
    session_id=request.COOKIES.get('session_id')

    if session_id is not None:
         authent=True
    else:
         authent=False
    try:
        sessioncust=Session_model.objects.get(session_id=session_id)
        print(sessioncust.user.Name)
        u=sessioncust.user
    except:
         print("not login")
    context={
         'authent':authent,
         'u':u
    }
    return render(request,'home.html',context)

def log(request):
    
    b=True
    user1=""
    if request.method=='POST':
        Name=request.POST.get('Name')
        password=request.POST.get('password')
        
        try:
                user = Customers.objects.get(Name=Name)
                user1=user
                print(user1)
                while True:
                        # Generate a random UUID for the session
                        session_id = str(uuid.uuid4())

                        try:
                            # Try to create a session with the generated session_id
                            session = Session_model.objects.create(session_id=session_id, user=user)
                            print("success")
                            break
                        except :
                            # If a session with the same session_id already exists, generate a new one
                            continue

                    # Set the session_id cookie and redirect to the home page
                response = redirect('home')
                response.set_cookie('session_id', session.session_id)
                return response
                

        except Customers.DoesNotExist:
            print("nonono")
            
            
            
        print("yes")
        session1=Session_model.objects.create(user=user)
                    
                    
               
                
           



       
    context={
        
    }

    return render(request,'loginform.html',context)
 

def logo(request):
    
    session_id=request.COOKIES.get('session_id')
    print(session_id)
    if session_id:
         
        response = redirect('home')
        response.delete_cookie('session_id')
        print("yes")
        return response

    context={
        
    }
    return render(request,'home.html',context)


def reg(request):
    n="nothing"
    form=Customers_forms()
    if request.method=='POST':
        name=request.POST.get('Name')
        print(name)
        form=Customers_forms(request.POST)
        if form.is_valid():


            try:
                n=None
                n=Customers.objects.get(Name=name)
                print("sorry we already have that name")
                
            except:
                user=Customers.objects.create(
                    Name=request.POST.get('Name'),
                    Username=request.POST.get('Username'),
                    Email=request.POST.get('Email'),
                    password=request.POST.get('password')
                )

                return redirect('home')
                
                
            
            
                
                

    context={
        'form':form,
    }
    return render(request,'registerform.html',context)



    