from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ServiceCategory, Service, Franchise, Enquiry, Carousel
from .forms import ServiceRequestForm, EnquiryForm


def ensure_franchise():
    """Ensure the franchise for CC9 exists (auto-create if missing)."""
    franchise, _ = Franchise.objects.get_or_create(
        code="CC9",
        defaults={"name": "Karnataka One CC9"}
    )
    return franchise


def home(request):
    """Homepage with categories, featured services, and carousel."""
    categories = ServiceCategory.objects.all()
    featured_services = Service.objects.filter(is_active=True)[:4]
    services = Service.objects.filter(is_active=True)
    carousel_items = Carousel.objects.filter(is_active=True)

    return render(request, "core/home.html", {
        "categories": categories,
        "featured_services": featured_services,
        "services": services,
        "carousel_items": carousel_items,
    })


def services(request):
    """List of all active services, optionally filtered by category."""
    category_id = request.GET.get("category")
    qs = Service.objects.filter(is_active=True).select_related("category")
    current_category = None
    if category_id:
        qs = qs.filter(category_id=category_id)
        current_category = ServiceCategory.objects.filter(id=category_id).first()
    categories = ServiceCategory.objects.all()
    return render(request, "core/services.html", {
        "services": qs,
        "categories": categories,
        "current_category": current_category,
    })


def service_detail(request, slug):
    """Service details + form to submit a request."""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            sr = form.save(commit=False)
            sr.service = service
            sr.franchise = ensure_franchise()
            sr.save()
            messages.success(request, "✅ Your request has been submitted. We will contact you soon.")
            return redirect("request_success")
    else:
        form = ServiceRequestForm()
    return render(request, "core/service_detail.html", {"service": service, "form": form})


def enquiry(request):
    """Enquiry form for users."""
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Thanks! Your enquiry has been received.")
            return redirect("enquiry")
    else:
        form = EnquiryForm()
    return render(request, "core/enquiry.html", {"form": form})


def request_success(request):
    """Success page after submitting a service request."""
    return render(request, "core/request_success.html")


def franchise(request):
    """Franchise information page (auto-created if missing)."""
    franchise = ensure_franchise()
    return render(request, "core/franchise.html", {"franchise": franchise})
