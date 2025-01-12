from django.shortcuts import render

# Create your views here.
def landing_view(request):
    return render(request, "layout/landing.html")

def home_view(request):
    return render(request, "layout/home.html")

def support_view(request):
    return render(request, "layout/support.html")

def account_view(request):
    return render(request, "layout/account.html")