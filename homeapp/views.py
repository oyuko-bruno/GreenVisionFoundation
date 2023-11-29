from django.shortcuts import render

# Create your views here.
def green(request):
    return render(request, 'index-2.html')

def act(request):
    return render(request, 'act-now.html')
    

def about(request):
    return render(request, 'about-1.html')

def service(request):
    return render(request, 'service.html')
    
def blog(request):
    return render(request, 'blog-full-with-right-sidebar.html')
    
def gallery(request):
    return render(request, 'gallery-3-columns-without-caption.html')

from django.shortcuts import render
"""
def act(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        address= request.POST.get("address")
        # Validate the data here
        if not first_name or not last_name or not email or not message:
            errors = ["Please fill in all required fields."]
        else:
            errors = []

        if not errors:
            # Process the data here
            # Save the data to a database, send an email, etc.

            # Send a success message
            success_message = "Your message has been sent!"

        context = {
            "errors": errors,
            "success_message": success_message,
        }
        return render(request, "act.html", context)
    else:
        context = {}
        return render(request, "act.html", context)"""
# myapp/views.py
# views.py
from django.shortcuts import render, redirect
from .forms import Contacts  # Correct the import to use Contact instead of ContactForm


 # myapp/views.py
from django.shortcuts import render, redirect
from .forms import FormDataForm

def form_submission(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = FormDataForm()

    return render(request, 'act-now.html', {'form': form})



