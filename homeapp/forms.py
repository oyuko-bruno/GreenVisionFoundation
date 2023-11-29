# forms.py
from django import forms
from .models import Contacts

# forms.py
from django import forms

class Contacts(forms.Form):
    # Define your form fields here
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

# myapp/forms.py
from django import forms
from .models import FormData

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['first_name', 'last_name', 'email', 'address', 'message']
