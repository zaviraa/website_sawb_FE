from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff: 
            login(request, user)
            return redirect("admin-home")  
        else:
            return render(request, "admin/login.html", {"error": "Invalid credentials or not an admin."})

    return render(request, "admin/login.html")

def admin_logout(request):
    if request.method == "POST":
        logout(request)  
        return redirect('admin-login') 
    return redirect('admin-home') 

@staff_member_required
def admin_home(request):
    return render(request, "admin/admin_home.html")

@staff_member_required
def admin_dashboard(request):
    return render(request, "admin/dashboard.html") 

@staff_member_required
def admin_blog(request):
    return render(request, "admin/admin_blog.html") 

@staff_member_required
def add_article(request):
    return render(request, "admin/add_article.html")

@staff_member_required
def all_article(request):
    return render(request, "admin/all-article.html")

@staff_member_required
def admin_about(request):
    return render(request, "admin/admin_about.html")

@staff_member_required
def admin_contact(request):
    return render(request, "admin/admin_contact.html")

@staff_member_required
def admin_article(request):
    return render(request, "admin/admin_article.html")

@staff_member_required
def article(request):
    return render(request, "admin/article.html")