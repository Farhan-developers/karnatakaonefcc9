from django.contrib import admin
from .models import Franchise, ServiceCategory, Service, Enquiry, Carousel, ServiceRequest

@admin.register(Franchise)
class FranchiseAdmin(admin.ModelAdmin):
    list_display = ("name", "code")

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "contact", "course", "created_at")
    search_fields = ("name", "email", "contact")
    
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("service", "franchise", "name", "email", "phone", "created_at")
