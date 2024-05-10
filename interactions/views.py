from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import ShowInterestForm, ContactSupplierForm
from .models import UserInterest
from market.models import Post
from users.models import Profile

@login_required
def show_interest(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ShowInterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.user = request.user
            interest.post = post
            interest.save()

            # Fetch the post owner's Profile
            post_owner_profile = get_object_or_404(Profile, user=post.author)
            post_owner_email = post_owner_profile.auth_mail # Assuming the email is directly accessible from the user model

            # Send notification to post owner
            send_mail(
                'Interest Notification',
                f'Someone showed interest in your post "{post.title}".',
                settings.DEFAULT_FROM_EMAIL,
                [post_owner_email],
                fail_silently=False,
            )
            return redirect('post-detail', pk=post_id)
    else:
        form = ShowInterestForm()
    return render(request, 'interactions/show_interest.html', {'form': form, 'post': post})



def contact_supplier(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Fetch the post
    if request.method == 'POST':
        form = ContactSupplierForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.post = post
            contact.save()

            # Fetch the post owner's Profile to get their email
            post_owner_profile = get_object_or_404(Profile, user=post.author)
            post_owner_email = post_owner_profile.auth_mail  # Assuming the email is directly accessible from the user model

            # Send email to post owner
            send_mail(
                'Supplier Contact Request from ' + contact.name,
                'Message: ' + contact.message, settings.DEFAULT_FROM_EMAIL,
                [post_owner_email],
                fail_silently=False,
            )
            return redirect('post-detail', pk=post_id)
    else:
        form = ContactSupplierForm()
    return render(request, 'interactions/contact_supplier.html', {'form': form, 'post': post})



def contact_success(request):
    return render(request, 'interactions/contact_success.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Render the email content from the template
            email_content = render_to_string('interactions/contact_email.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            })

            # Send email
            send_mail(
                subject,
                email_content,
                'himanshusanjaykhale@gmail.com',  # From email
                ['codexautomationkey@gmail.com'],  # To email
                fail_silently=False,
                html_message=email_content  # For HTML emails
            )

            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'interactions/contact.html', {'form': form})