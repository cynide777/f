"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from lab1.views import current_datetime,fha,fhb,fhao,fhbo
from lab21.views import show_list,home,contactus,aboutus
from lab22.views import register, viewstudent, displaystudents,add_project
from lab22.views import StudentListView, StudentDetailView
from lab22.views import StudentListView, StudentDetailView, download, generate_pdf
from lab31.views import registerAJ,searchAJ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cdt/',current_datetime),
    path('fha/',fha),
    path('fhb/',fhb),
    path('fhao/<int:offset>',fhao),
    path('fhbo/<int:offset>',fhbo),
    path('showlist/',show_list),
    path('home/',home),
    path('about/',aboutus),
    path('contact/',contactus),
    path('register/',register),
    path('viewstudent/',viewstudent),
    path('viewstudent/displaystudents/',displaystudents),
    path('add_project/',add_project),
    path('student_list/',StudentListView.as_view()),
    path('student_list/student_detail/<int:pk>/',StudentDetailView.as_view()),
    path('download/',download),
    path('generate_pdf_file/',generate_pdf),
    path('registerAJ/',registerAJ),
    path('searchAJ/',searchAJ),




]
