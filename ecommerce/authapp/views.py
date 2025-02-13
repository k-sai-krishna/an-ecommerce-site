from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method == 'POST':
        print("It is POST method")
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(username)
        if password != confirm_password:
            return HttpResponse("Password doesn't match")
        try:
            # from django.contrib.auth.models import User
            # User is a defalut table provided by django
            if User.objects.get(username=username):
                return HttpResponse("User already exists")
        except:
            pass
        user = User.objects.create_user(username, username, password)
        user.save()
        return HttpResponse("User created successfully")
    else:
        print("It is GET method")
    
    return render(request,'authentication/signup.html')
def login(request):
    return render(request,'authentication/login.html')
def logout(request):
    return redirect('/auth/login/')