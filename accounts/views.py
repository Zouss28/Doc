from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def login_view(request):
    context = {}
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        context = {'error':'Wrong username or password'}
    return render(request, 'accounts/login.html',{"context":context})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'accounts/logout.html',{})