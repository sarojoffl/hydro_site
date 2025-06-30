from django import forms
from .models import (
    AboutInfo, AboutImage, Fact,
    CarouselItem,
    Feature, FeatureImage,
    Service, Project,
    TeamMember, Testimonial,
    Download, Report, Notice,
    Client, ContactInfo,
    OrganizationDetail,
)

class CarouselItemForm(forms.ModelForm):
    class Meta:
        model = CarouselItem
        fields = ['title', 'subtitle', 'image', 'button_text', 'button_link']

class AboutInfoForm(forms.ModelForm):
    class Meta:
        model = AboutInfo
        fields = ['heading', 'description', 'years_experience', 'email', 'phone', 'features']
        widgets = {
            'features': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter features as a comma-separated list'}),
        }

class AboutImageForm(forms.ModelForm):
    class Meta:
        model = AboutImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(),
        }

class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = ['icon_class', 'number', 'label']
        widgets = {
            'icon_class': forms.TextInput(attrs={'placeholder': 'e.g., fas fa-trophy'}),
            'number': forms.NumberInput(attrs={'min': 0}),
            'label': forms.TextInput(attrs={'placeholder': 'e.g., Awards'}),
        }

class FeatureImageForm(forms.ModelForm):
    class Meta:
        model = FeatureImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(),
        }

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['icon_class', 'title', 'description']
        widgets = {
            'icon_class': forms.TextInput(attrs={'placeholder': 'e.g., fas fa-cog'}),
            'title': forms.TextInput(attrs={'placeholder': 'Feature Title'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Feature Description'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Service Title'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Service Description'}),
            'image': forms.ClearableFileInput(),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'link', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Project Title'}),
            'image': forms.ClearableFileInput(),
            'link': forms.URLInput(attrs={'placeholder': 'Project Link (optional)'}),
            'status': forms.Select(),
        }

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'photo', 'facebook', 'twitter', 'instagram']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Team Member Name'}),
            'position': forms.TextInput(attrs={'placeholder': 'Position'}),
            'photo': forms.ClearableFileInput(),
            'facebook': forms.URLInput(attrs={'placeholder': 'Facebook URL (optional)'}),
            'twitter': forms.URLInput(attrs={'placeholder': 'Twitter URL (optional)'}),
            'instagram': forms.URLInput(attrs={'placeholder': 'Instagram URL (optional)'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'profession', 'photo', 'text']
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder': 'Client Name'}),
            'profession': forms.TextInput(attrs={'placeholder': 'Profession'}),
            'photo': forms.ClearableFileInput(),
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Testimonial Text'}),
        }

class DownloadForm(forms.ModelForm):
    class Meta:
        model = Download
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Download Title'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Description (optional)'}),
            'file': forms.ClearableFileInput(),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Report Title'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Description (optional)'}),
            'file': forms.ClearableFileInput(),
        }

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Notice Title'}),
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Notice Content'}),
            'attachment': forms.ClearableFileInput(),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'logo', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Client Name'}),
            'logo': forms.ClearableFileInput(),
            'website': forms.URLInput(attrs={'placeholder': 'https://'}),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['phone_number', 'email', 'office_address', 'map_link', 'map_iframe_src']
        widgets = {
            'office_address': forms.Textarea(attrs={'rows': 2}),
            'map_iframe_src': forms.Textarea(attrs={'rows': 3}),
        }

class OrganizationDetailForm(forms.ModelForm):
    class Meta:
        model = OrganizationDetail
        fields = [
            'site_title', 'address', 'phone', 'whatsapp_number', 'email',
            'weekday_hours', 'saturday_hours', 'sunday_hours',
            'facebook', 'twitter', 'instagram', 'linkedin',
        ]
        widgets = {
            'site_title': forms.TextInput(attrs={'placeholder': 'Site Title'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'WhatsApp Number (optional)'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'weekday_hours': forms.TextInput(attrs={'placeholder': 'Monday - Friday hours'}),
            'saturday_hours': forms.TextInput(attrs={'placeholder': 'Saturday hours'}),
            'sunday_hours': forms.TextInput(attrs={'placeholder': 'Sunday hours'}),
            'facebook': forms.URLInput(attrs={'placeholder': 'Facebook URL'}),
            'twitter': forms.URLInput(attrs={'placeholder': 'Twitter URL'}),
            'instagram': forms.URLInput(attrs={'placeholder': 'Instagram URL'}),
            'linkedin': forms.URLInput(attrs={'placeholder': 'LinkedIn URL'}),
        }