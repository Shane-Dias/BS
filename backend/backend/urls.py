"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from incidents import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/report-incident/', views.form_report.as_view(), name='report_incident'),
    path('api/', include('incidents.urls')),
    path('api/signup/', views.SignUpView.as_view(), name='signup'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/send_email', views.send_email_example, name='send_email'),
    path('api/latest-incidents/', views.latest_incidents, name='latest-incidents'),
    path("api/user/<int:user_id>/", views.UserDetailView.as_view(), name="user-detail"),
]

'''path('report-incident/', views.post, name='report_incident'),'''