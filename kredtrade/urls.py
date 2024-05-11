"""
URL configuration for kredtrade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
#from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from item import views as item_views
from interactions import views as interactions_views

#from item.views import ItemCreateView




urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('market.urls')),
    path('item/', include('item.urls')),
    path('register/', user_views.register, name = 'register'),
    path('profile/<int:pk>/', user_views.profile, name = 'profile' ),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    path('item/<int:pk>/', item_views.detail, name = 'item-detail'),
    path('profileupdate/<int:pk>/', user_views.profileupdate, name='profile-update'),
    path('profileupdate-certificates/<int:pk>', user_views.certificateupdate, name = 'certificate-update'),
    path('profileupdate-factory/<int:pk>', user_views.factoryupdate, name = 'factory-update'),
    path('profileupdate-personnel/<int:pk>', user_views.personnelupdate, name = 'personnel-update'),
    path('profileupdate-certificate/', user_views.add_certificate, name = 'add-certificate'),
    path('edit_certificate/<int:pk>/', user_views.edit_certificate, name='edit-certificate'),
    path('delete_certificate/<int:pk>/', user_views.delete_certificate, name='delete-certificate'),
    path('item/new/', item_views.newitem, name = 'new-item'),
    path('item/delete/<int:pk>/', item_views.delete, name='delete-item'),
    path('item/edit/<int:pk>/', item_views.edititem, name='edit-item'),
    path('item/all-items/', item_views.items, name = 'all-items'),
    path('publicprofile/<int:pk>/', user_views.public_profile, name = 'public-profile' ),
    path('market/', include(('market.urls', 'market'), namespace = 'categories')),
    
    path('show_interest/<int:post_id>/', interactions_views.show_interest, name='show_interest'),
    path('contact_supplier/<int:post_id>/', interactions_views.contact_supplier, name='contact_supplier'),

    path('contact/', interactions_views.contact, name='contact'),
    path('contact_success/', interactions_views.contact_success, name='contact_success'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include default auth URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    
    #path('item/list/', ItemCreateView.as_view(), name = 'item-create')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
