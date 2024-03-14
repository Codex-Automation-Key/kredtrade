from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, RegistrationCertificate, State, City
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
import datetime
from django.core.validators import FileExtensionValidator



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


INPUT_CLASSES = 'mt-6 w-auto py-3 px-3 rounded-xl border '


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image', 'company', 'address','est', 
                'nature', 'turnover', 'status', 
                'description', 'employee', 'state']
        labels = {
             
            'company': 'Company Name',
            'image': 'Company Logo', 
            'address': 'Company Address',
            'est': 'Year Of Establishment', 
            'nature': 'Nature of Company', 
            'turnover': 'Annual Turnover', 
            'status': 'Legal Status', 
            'description': 'About the company', 
            'employee': 'Number of Employees',
            'state': 'State',


        }

        widgets = {
        
        'company': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'address': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'est': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'nature': forms.Select(choices=Profile.NATURE_CHOICES),

        'turnover': forms.Select(choices=Profile.TURNOVER_CHOICES),

        'status': forms.Select(choices=Profile.STATUS_CHOICES),

        'description': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'address': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'employee': forms.Select(choices=Profile.EMPLOYEE_CHOICES),

        'state': forms.Select(choices=Profile.STATE_CHOICES)

        

        }
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': INPUT_CLASSES}))

    



class CertificateUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gst_no',
                'gst',  
                'pan_no',
                'pan',  
                'udyam_no',
                'udyam',  
                'iec_no',
                'iec',]
        
        labels = {
            'gst_no' : 'GST Number',
            'pan_no': 'PAN Number', 
            'udyam_no': 'Udyam Aadhar Number', 
            'iec_no': 'Import Export Code',
            'gst': 'Upload GST Certificate', 
            'pan': 'Upload PAN Card', 
            'udyam': 'Upload Udyam Aadhar', 
            'iec': 'Upload IEC Certificate', 

        }
        widgets = {
            'gst_no': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'pan_no': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'udyam_no': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'iec_no': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'gst': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'pan': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'udyam': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'iec': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }



class FactoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['factoryaddress', 'factorydesc', 
                    'factorytype']
        
        labels = {
            'factoryaddress': 'Factory Address', 
            'factorydesc': 'Factory Description', 
            'factorytype': 'Factory Type', 
        }
        
        widgets = {
        
        'factoryaddress': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'factorydesc': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'factorytype': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
    }



class PersonnelUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['promotor_name', 'promotror_mail', 
                'promotor_mob', 'auth_name', 
                'auth_mail', 'auth_mob']
        labels = {
            'promotor_name': 'Name: Promotor', 
            'promotror_mail': "Email ID: Promotor", 
            'promotor_mob': "Contact Number: Promotor", 
            'auth_name': "Name: Authorized Person", 
            'auth_mail': "Email ID: Authorized Person", 
            'auth_mob': "Contact Number: Authorized Person"
        }
        widgets = {
        
        'promotor_name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'promotror_mail': forms.EmailInput(attrs={
            'class': INPUT_CLASSES
        }),
        'promotor_mob': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'auth_name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        
        'auth_mail': forms.EmailInput(attrs={
            'class': INPUT_CLASSES
        }),
        
        'auth_mob': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),

    }
class RegistrationCertificateForm(forms.ModelForm):
    certificate_file = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'input-classes',  # Replace 'input-classes' with your actual CSS class
            'accept': '.pdf'  # This restricts the file picker dialog to only show .pdf files
        }),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        label='Upload Your Certificate'
    )

    class Meta:
        model = RegistrationCertificate
        fields = ['certificate_name', 'certificate_file', 'issued_by', 'issue_date', 'valid_until']

        labels = {
            'certificate_name': 'Certificate Name', 
            
            'issued_by': 'Certificate Issuing Authority', 
            'issue_date': 'Issued On', 
            'valid_until': 'Valid Till'
        }

        widgets = {
            'certificate_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES  # Replace 'input-classes' with your actual CSS class
            }),
            'issued_by': forms.TextInput(attrs={
                'class': INPUT_CLASSES  # Replace 'input-classes' with your actual CSS class
            }),
            'issue_date': forms.DateInput(attrs={
                'type': 'date',
                'class': INPUT_CLASSES  # Replace 'input-classes' with your actual CSS class
            }),
            'valid_until': forms.DateInput(attrs={
                'type': 'date',
                'class': INPUT_CLASSES # Replace 'input-classes' with your actual CSS class
            }),
        }


