from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about', views.about_page,name='about_page'),
    path('service', views.service_page,name='service_page'),
    path('contact', views.contact_page,name='contact_page'),
    path('blog', views.blogg_page,name='blogg_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('thankyou', views.thanks_view,name='thanks_view'),
    #path('freequote', views.newletter_view,name='newletter_view'),
    #path('newletter', views.freequote_view,name='freequote_view'),
]