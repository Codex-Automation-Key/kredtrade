from django import forms
from .models import UserInterest, SupplierMessage

INPUT_CLASSES = 'mt-6 w-auto py-3 px-3 rounded-xl border '


class ShowInterestForm(forms.ModelForm):
    class Meta:
        model = UserInterest
        fields = []

class ContactSupplierForm(forms.ModelForm):
    class Meta:
        model = SupplierMessage
        fields = ['name', 'email', 'message']
        
        labels = {
            'name': 'Name',
            'email': 'Your email id',
            'message': 'Your message',
        }

        widgets = {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
            'class': INPUT_CLASSES
            }),
            'message': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
        }
