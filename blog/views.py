from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

from .models import Post, FreeQuote
from .forms import PostForm, FreequoteForm

def post_list(request):
    form = FreequoteForm(request.POST or None)
    success =False
    if request.method == "POST":
    	if form.is_valid():
    		form.save()
    		form = FreequoteForm()
    		success = True
    		messages.success(request, 'Your Free quote request has been submited. Thank you')
    return render(request, 'home.html', {'form': form})

def about_page(request):
    return render(request, 'about.html', {})

def service_page(request):
    return render(request, 'service.html', {})

def blogg_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogg.html', {'posts': posts})

def contact_page(request):
    form = PostForm(request.POST or None)
    success = False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = PostForm()
            success =True
            messages.success(request, 'Your Message has been submitted, our team will be intouch soon.')
    return render(request, 'contact.html', {'form': form})

def newletter_view(request):
    return render(request, 'newletter.html', {})

def freequote_view(request):
    return render(request, 'freequote.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_details.html', {'post': post})

def thanks_view(request):
    return render(request, 'Thank_page.html')

