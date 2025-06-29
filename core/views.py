from django.shortcuts import render

def home(request): return render(request, 'home.html')
def about(request): return render(request, 'about.html')
def services(request): return render(request, 'services.html')
def projects(request): return render(request, 'projects.html')
def reports(request): return render(request, 'reports.html')
def downloads(request): return render(request, 'downloads.html')
def notice(request): return render(request, 'notice.html')
def contact(request): return render(request, 'contact.html')
