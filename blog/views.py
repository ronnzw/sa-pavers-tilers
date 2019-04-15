from django.shortcuts import render


def post_list(request):
    return render(request, 'home.html', {})

def about_page(request):
    return render(request, 'about.html', {})

def service_page(request):
    return render(request, 'service.html', {})

# Create your views here.
