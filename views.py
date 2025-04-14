from django.shortcuts import render

def index(request):
    return render(request, 'user/index.html')

def about(request):
    return render(request, 'user/about.html')

def contact(request):
    return render(request, 'user/contact.html')

def blog(request):
    return render(request, 'user/blog.html')
