from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("service/<slug:slug>/", views.service_detail, name="service_detail"),
    path("enquiry/", views.enquiry, name="enquiry"),
    path("request-success/", views.request_success, name="request_success"),
    path("franchise/", views.franchise, name="franchise"),
]
