from django import forms
from .models import ServiceRequest, Enquiry


class BaseBootstrapForm(forms.ModelForm):
    """
    Base form to automatically apply Bootstrap's 'form-control' class
    to all input fields (except checkboxes and radio buttons).
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                existing = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = (existing + ' form-control').strip()


class ServiceRequestForm(BaseBootstrapForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'phone', 'email', 'document']  # ✅ matches model
        widgets = {
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class EnquiryForm(BaseBootstrapForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'contact', 'course', 'message']  # ✅ matches model
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
