from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    return render(request,'authentication/login.html')
def signup(request):
    return render(request,'authentication/signup.html')
def logout(request):
    return redirect('/auth/login')