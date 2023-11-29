from django.shortcuts import render
from .forms import DonorRegistration
from .models import DonorList
from django.contrib import messages


#Donnor forms display
#def donorregdisplay(request):
  #  forms = DonorRegistration()
   # if request.method == 'POST':
     #   forms = DonorRegistration(request.POST)
     #   if forms.is_valid():
        #    forms.save()
         #   print(forms.errors)
          #  context_details ={
           #     'forms' : forms
           # }
            #After donor registation donor details display
           # return render(request, 'donor_reg_s.html', context_details)

    #context = {
       #         'forms' : forms,
         #   }


  #  return render(request, 'donor_reg.html', context)

# views.py
from django.shortcuts import render
from .forms import DonorRegistration
from .models import DonorList

def donorregdisplay(request):
    forms = DonorRegistration()
    if request.method == 'POST':
        forms = DonorRegistration(request.POST)
        if forms.is_valid():
            instance = forms.save()  # Assuming your form is based on a model
            context_details = {
                'forms': forms,
                'id': instance.id,  # Pass the id to the context
            }
            return render(request, 'donor_reg_s.html', context_details)

    context = {
        'forms': forms,
    }

    return render(request, 'donor_reg.html', context)

    
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DonorList

def updateData(request, id):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        occupation = request.POST.get("occupation")
        home_address = request.POST.get("home_address")
        last_donate_date = request.POST.get("last_donate_date")
        tree_donate = request.POST.get("tree_donate")
        phone_number = request.POST.get("phone_number")

        rekebisha = DonorList.objects.get(id=id)
        rekebisha.name = name
        rekebisha.email = email
        rekebisha.gender = gender
        rekebisha.occupation = occupation
        rekebisha.home_address = home_address
        rekebisha.last_donate_date = last_donate_date
        rekebisha.tree_donate = tree_donate
        rekebisha.phone_number = phone_number
        rekebisha.save()

        messages.success(request, 'Your information updated successfully!')
        return redirect('donor_reg_s.html')
    else:
        d = DonorList.objects.get(id=id)
        return render(request, 'edit.html', {'d': d})


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import DonorList



def delete(request, id):
    try:
        donor = get_object_or_404(DonorList, id=id)
        donor.delete()
        return redirect('/')
    except DonorList.DoesNotExist:
        # Handle the case where the DonorList does not exist
        # You might want to show an error message or redirect to an error page
        error_message = f"DonorList with id {id} does not exist."
        return render(request, 'error_page.html', {'error_message': error_message})

