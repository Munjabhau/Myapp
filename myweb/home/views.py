from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Contact, test


# Create your views here.
def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request, 'username must be unser 10 character ')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account created")
        return redirect('home')
    else:
        return HttpResponse("404 not found")


def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('home')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logout")
    return redirect('home')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "please fill details correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your response has been submited successfully")
    return render(request, "home/contact.html")


def stdDetails(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        standard = request.POST['standard']
        details = test(name=name, address=address, standard=standard)
        details.save()
        messages.success(request, "Details store successfully")
    return render(request, "home/test.html")
