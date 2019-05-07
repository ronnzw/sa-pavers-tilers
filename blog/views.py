from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

from .models import Post, FreeQuote, Newletter
from .forms import PostForm, FreequoteForm, NewletterForm

def post_list(request):
    form = FreequoteForm(request.POST or None)
    success =False
    if request.method == "POST":
    	if form.is_valid():
    		form.save()
    		form = FreequoteForm()
    		success = True
    		messages.success(request, 'Your Free quote request has been submited. Thank you')

    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form = NewletterForm()
    return render(request, 'home.html', {'form': form, 'sub_form': sub_form})

def about_page(request):
    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form = NewletterForm()  
    return render(request, 'about.html', {'sub_form': sub_form})

def service_page(request):
    form = FreequoteForm(request.POST or None)
    success =False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = FreequoteForm()
            success = True
            messages.success(request, 'Your Free quote request has been submited. Thank you')

    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form =NewletterForm()                
    return render(request, 'service.html', {'form': form, 'sub_form': sub_form})

def blogg_page(request):
    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form =NewletterForm()    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogg.html', {'posts': posts, 'sub_form': sub_form})

def contact_page(request):
    form = PostForm(request.POST or None)
    success = False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = PostForm()
            success =True
            messages.success(request, 'Your Message has been submitted, our team will be intouch soon.')
    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form =NewletterForm()            
    return render(request, 'contact.html', {'form': form, 'sub_form': sub_form})

def newletter_view(request):
    form = NewletterForm(request.POST or None)
    success =False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = NewletterForm()
            success = True
            messages.success(request, 'Newletter request has been submitted')    
    return render(request, 'newletter.html', {'form': form})

def freequote_view(request):
    return render(request, 'freequote.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_details.html', {'post': post})

def thanks_view(request):
    return render(request, 'Thank_page.html')

