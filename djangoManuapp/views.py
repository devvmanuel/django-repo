from django.shortcuts import render,redirect



def signup(request):
    return render(request, "signup.html")

def indexpage(request):
    return render(request, "index.html")

def aboutpage(request):
    return render(request, "about.html")



def servicespage(request):
    return render(request , "services.html")


def blogpage(request):
    return render(request , "blog.html")



def projectspage(request):
    return render(request , "projects.html")