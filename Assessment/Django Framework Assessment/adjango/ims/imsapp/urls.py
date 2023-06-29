"""
URL configuration for DigitalSociety project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from imsapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('change-password/', views.change_password, name ='change-password'),
    path('update-chairman-profile', views.update_chairman_profile, name = 'update-chairman-profile'),
    path('add-media/',views.add_media,name='add-media'),
    path('view-image-gallery',views.view_image_gallery,name='view-image-gallery'),
    path('view-video-gallery',views.view_video_gallery,name='view-video-gallery'),
    path('delete-video/<int:pk>',views.delete_video,name='delete-video'),
    path('delete-image/<int:ik>',views.delete_image,name='delete-image'),
    path('add-member/',views.add_member,name='add-member'),
    path('all-member/',views.all_member,name='all-member'),
    path('sall-member/',views.sall_member,name='sall-member'),
    path('add-notice',views.add_notice,name='add-notice'),
    path('all-notices/',views.all_notices,name='all-notices'),
    path('sall-notices/',views.sall_notices,name='sall-notices'),


]
