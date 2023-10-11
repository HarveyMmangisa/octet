from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

# views.py
def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'coming.html')

def detail(request):
    return render(request, 'coming.html')

def feature(request):
    return render(request, 'coming.html')

def price(request):
    return render(request, 'coming.html')

def quote(request):
    return render(request, 'coming.html')

def team(request):
    return render(request, 'coming.html')

def testimonial(request):
    return render(request, 'coming.html')


def contact(request):
    return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, email, [''])
            return render(request, 'contact.html', {'form': form, 'message': 'Email sent successfully'})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})