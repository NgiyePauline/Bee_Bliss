from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def quality(request):
    return render(request, 'quality.html')

def shop(request):
    return render(request, 'shop.html')

def base(request):
    return render(request, 'base.html')
