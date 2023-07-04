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
    path('', views.dashboard, name='dashboard'),
    path('home/',views.home,name='home'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('teacher/', views.teacher, name ='teacher'),
    path('s_teacher/', views.s_teacher, name ='s_teacher'),
    path('s_profile',views.s_profile,name='s_profile'),
    path('change-password/', views.change_password, name ='change-password'),
    path('update-teacher-profile', views.update_teacher_profile, name = 'update-teacher-profile'),
    path('update-student-profile', views.update_student_profile, name = 'update-student-profile'),
    path('student/',views.student,name='student'),
    path('s_student/',views.s_student,name='s_student'),
    path('register',views.register,name='register'),
    path('clubs',views.clubs,name='clubs'),
    path('library',views.library,name='library'),
    path('events',views.events,name='events'),
    path('campus',views.campus,name='campus'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('resetpassword',views.resetpassword,name='resetpassword'),
    
]
