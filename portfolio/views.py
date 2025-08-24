from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def home_page(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, "contact.html")



def projects(request):
    return render(request, "projects.html")