from django.shortcuts import render
from .models import Document
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, ContactForm


# View for Index Page Documents
def index(request):
    documents = Document.objects.filter(page='index')
    return render(request, 'index.html', {'documents': documents})

# View for About Page Documents
def about(request):
    documents = Document.objects.filter(page='about')
    return render(request, 'about.html', {'documents': documents})

# View for Services Page Documents
def services(request):
    documents = Document.objects.filter(page='services')
    return render(request, 'services.html', {'documents': documents})

# View for Register Page Documents
# def register(request):
#     documents = Document.objects.filter(page='register')
#     return render(request, 'register.html', {'documents': documents})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')  # Redirect to login page after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('index')  # Redirect to the home page if login is successful

                
                
        else:
            messages.error(request, 'Invalid username or password')  # Show an error message

    return render(request, 'login.html')



# View for handling the contact form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send the email
            send_mail(
                f"New Contact Form Submission from {name}",
                f"Message from {name} ({email}):\n\n{message}",
                settings.DEFAULT_FROM_EMAIL,  # From email
                ['your-recipient-email@example.com'],  # Replace with your email
                fail_silently=False,
            )
            # Optional: redirect to a success page after email is sent
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    
    return render(request, 'uae.html', {'form': form})

# View for Reports Page Documents
def data_scrapping(request):
    documents = Document.objects.filter(page='data_scrapping')
    return render(request, 'reports.html', {'documents': documents})

# View for CS Page Documents
def survey(request):
    documents = Document.objects.filter(page='cs')
    return render(request, 'cs.html', {'documents': documents})

# View for ML Page Documents
def ml(request):
    documents = Document.objects.filter(page='ml')
    return render(request, 'ml.html', {'documents': documents})

# View for Economics Page Documents
def economics(request):
    documents = Document.objects.filter(page='economics')
    return render(request, 'economics.html', {'documents': documents})

# View for Data Analysis Page Documents
def data_analysis(request):
    documents = Document.objects.filter(page='data_analysis')
    return render(request, 'data_analysis.html', {'documents': documents})

# View for Data Mining Page Documents
def data_cleaning(request):
    documents = Document.objects.filter(page='data_mining')
    return render(request, 'data_mining.html', {'documents': documents})

# View for Finance Page Documents
def finance(request):
    documents = Document.objects.filter(page='finance')
    return render(request, 'finance.html', {'documents': documents})

# View for Business Analytics Page Documents
def business_analytics(request):
    documents = Document.objects.filter(page='business_analytics')
    return render(request, 'business_analytics.html', {'documents': documents})

# View for Case Studies Page Documents
def data_insights(request):
    documents = Document.objects.filter(page='data_insights')
    return render(request, 'case_studies.html', {'documents': documents})

# View for Business Page Documents
def business_forecasting(request):
    documents = Document.objects.filter(page='business_forecasting')
    return render(request, 'business.html', {'documents': documents})

# View for Marketing Page Documents
def predictive_analysis(request):
    documents = Document.objects.filter(page='predictive_analysis')
    return render(request, 'marketing.html', {'documents': documents})

# View for Research Page Documents
def data_visualization(request):
    documents = Document.objects.filter(page='data_visualization')
    return render(request, 'research.html', {'documents': documents})


# View for the technical writing section

def technical_writing(request):
    return render(request, 'technical_writing.html', {})

def exams(request):
    return render(request, 'exams.html', {})

# View for Data Analysis Page Documents
def singapore(request):
    documents = Document.objects.filter(page='singapore')
    return render(request, 'singapore.html', {'documents': documents})
# View for Data Analysis Page Documents
def uae(request):
    documents = Document.objects.filter(page='uae')
    return render(request, 'uae.html', {'documents': documents})





def assignment(request):
    return render(request, 'assignment.html', {})