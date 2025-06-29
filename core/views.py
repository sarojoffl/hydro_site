from django.shortcuts import render
from .models import (
    ContactInfo, ContactMessage, CarouselItem, AboutImage, AboutInfo,
    Fact, Feature, Service, Project, TeamMember, Testimonial, FeatureImage
)
from .forms import ContactForm


# Home Page View
def home(request):
    context = {
        'carousel_items': CarouselItem.objects.all(),
        'about_images': AboutImage.objects.all(),
        'about_info': AboutInfo.objects.first(),
        'facts': Fact.objects.all(),
        'feature_img': FeatureImage.objects.first(),
        'features': Feature.objects.all(),
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'team_members': TeamMember.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'contact_info': ContactInfo.objects.first(),
    }
    return render(request, 'home.html', context)


# About Page View
def about(request):
    context = {
        'about_images': AboutImage.objects.all(),
        'about_info': AboutInfo.objects.first(),
        'facts': Fact.objects.all(),
        'team_members': TeamMember.objects.all(),
        'contact_info': ContactInfo.objects.first(),
    }
    return render(request, 'about.html', context)


# Static Pages
def services(request):
    context = {
        'services': Service.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }

    return render(request, 'services.html', context)

def projects(request):
    return render(request, 'projects.html')

def reports(request):
    return render(request, 'reports.html')

def downloads(request):
    return render(request, 'downloads.html')

def notice(request):
    return render(request, 'notice.html')


# Contact Page View
def contact(request):
    contact_info = ContactInfo.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactMessage.objects.create(
                name=cd['name'],
                email=cd['email'],
                subject=cd['subject'],
                message=cd['message']
            )
            return render(request, 'contact.html', {
                'form': ContactForm(),
                'success': True,
                'contact_info': contact_info,
            })
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'contact_info': contact_info,
    })
