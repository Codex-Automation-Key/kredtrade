from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ( UserRegisterForm, 
                    UserUpdateForm, 
                    ProfileUpdateForm, 
                    CertificateUpdateForm, 
                    FactoryUpdateForm, 
                    PersonnelUpdateForm,
                    RegistrationCertificateForm,
)                    
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from market.models import Post, Industry, Category
from item.models import Item
from users.models import RegistrationCertificate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView,
                                DeleteView
)




def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, now you can login and explore the platform!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

'''
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if self.next_page is not None:
           # Redirect to 'next_page' on GET request
            self.next_page = request.GET.get('next', self.next_page)
        return super().dispatch(request, *args, **kwargs)
'''
def user_logout(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'market/home.html')

@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    reg_certificates = RegistrationCertificate.objects.filter(user=user)[0:3]
    profile = user.profile
    
    # Process certificates to filter out defaults and prepare them for the template

    context = {
        'posts':Post.objects.filter(author = user).order_by('-date_posted')[0:3],
        'items':Item.objects.filter(created_by = user).order_by('-created_at')[0:3],
        'user':user,
        'profile':profile,
        'reg_certificates':reg_certificates
        

    }

    return render(request, 'users/profile.html', context)

class ProfileUpdateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = ProfileUpdateForm
    template_name = 'users/profile-update.html'



@login_required
def profileupdate(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance = request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Account Updated!')
            

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
       

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'posts':Post.objects.all(),
        'items':Item.objects.all(),
        'users':User.objects.all(),
        
    }
    return render(request, 'users/profile-update.html', context)

@login_required
def certificateupdate(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':

       
        c_form = CertificateUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance = request.user.profile)
        
        if c_form.is_valid():
            c_form.save()
           
            
            messages.success(request, f'Account Updated!')
            
    else:
       
        c_form = CertificateUpdateForm(instance = request.user.profile)
       

    context = {
        'c_form' : c_form,
        
        'posts':Post.objects.all(),
        'items':Item.objects.all(),
        'users':User.objects.all(),
        
    }
    return render(request, 'users/certificate-update.html', context)



@login_required
def factoryupdate(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':

        
        f_form = FactoryUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance = request.user.profile)
        
        if f_form.is_valid(): 
            f_form.save()
            
            
            messages.success(request, f'Factory details updated!')
            

    else:
        
        f_form = FactoryUpdateForm(instance = request.user.profile)
       

    context = {
        'f_form' : f_form,
        
        'posts':Post.objects.all(),
        'items':Item.objects.all(),
        'users':User.objects.all(),
        
    }
    return render(request, 'users/factory-update.html', context)


@login_required
def personnelupdate(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':

        
        ap_form = PersonnelUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance = request.user.profile)
        
        if ap_form.is_valid():
            ap_form.save()
            
            messages.success(request, f'Personnel Details Updated!')
            
    else:
        
        ap_form = PersonnelUpdateForm(instance = request.user.profile)
       

    context = {
        'ap_form' : ap_form,
        
        'posts':Post.objects.all(),
        'items':Item.objects.all(),
        'users':User.objects.all(),
        
    }
    return render(request, 'users/personnel-update.html', context)







def public_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    user_posts = Post.objects.filter(author=user).order_by('-date_posted')
    items = Item.objects.filter(created_by = user).order_by('-created_at')
    reg_certificates = RegistrationCertificate.objects.filter(user=user)[0:3]
    profile = user.profile
    
    # Process certificates to filter out defaults and prepare them for the template
    certificates = {
        'GST Number': profile.gst_no if profile.gst_no != 'N/A' else None,
        'PAN Number': profile.pan_no if profile.pan_no != 'N/A' else None,
        'Udyam Aadhar Number': profile.udyam_no if profile.udyam_no != 'N/A' else None,
        'Import Export Code': profile.iec_no if profile.iec_no != 'N/A' else None,
        'FSSAI Registration': profile.fssai_no if profile.fssai_no != 'N/A' else None,
        # Add other fields as necessary
    }
    # Filter out None values
    certificates = {k: v for k, v in certificates.items() if v is not None}

    context = {
        'user': user,
        'certificates': certificates,
        'user_posts': user_posts,
        'items': items, 
        'profile': profile,
        'reg_certificates':reg_certificates
      
        # Include other context data as necessary
    }
    return render(request, 'users/public-profile.html', context)


@login_required
def add_certificate(request):
    if request.method == 'POST':
        form = RegistrationCertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.save()
            return redirect('profile', pk=request.user.pk)
    else:
        form = RegistrationCertificateForm()
    return render(request, 'users/add_certificate.html', {'form': form})

@login_required
def edit_certificate(request, pk):
    certificate = get_object_or_404(RegistrationCertificate, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RegistrationCertificateForm(request.POST, request.FILES, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=request.user.pk)
    else:
        form = RegistrationCertificateForm(instance=certificate)
    return render(request, 'users/edit_certificate.html', {'form': form, 'certificate': certificate})

@login_required
def delete_certificate(request, pk):
    certificate = get_object_or_404(RegistrationCertificate, pk=pk, user=request.user)
    if request.method == 'POST':
        certificate.delete()
        return redirect('profile', pk=request.user.pk)
    return render(request, 'users/delete_certificate_confirm.html', {'certificate': certificate})