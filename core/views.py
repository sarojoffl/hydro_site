from django.shortcuts import render
from .models import ContactInfo, ContactMessage
from .forms import ContactForm

def home(request): return render(request, 'home.html')
def about(request): return render(request, 'about.html')
def services(request): return render(request, 'services.html')
def projects(request): return render(request, 'projects.html')
def reports(request): return render(request, 'reports.html')
def downloads(request): return render(request, 'downloads.html')
def notice(request): return render(request, 'notice.html')
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
