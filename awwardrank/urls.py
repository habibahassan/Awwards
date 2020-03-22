from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include



urlpatterns=[
    path('', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',views.home, name='home'),
    path('project/(?P<project_id>[0-9])',views.project,name ='project'),
    path('profile/',views.profile, name='profile'),
    path('post/', views.upload_form, name='post'),
    path('edit/', views.edit_prof, name='edit'),

]
