from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post

def post_list(request):
    return render(request, 'home.html', {})

def about_page(request):
    return render(request, 'about.html', {})

def service_page(request):
    return render(request, 'service.html', {})

def blogg_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogg.html', {'posts': posts})

def contact_page(request):
    return render(request, 'contact.html', {})

def newletter_view(request):
    return render(request, 'newletter.html', {})

def freequote_view(request):
    return render(request, 'freequote.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_details.html', {'post': post})

