from django.urls import path
from . import views
from .views import show_interest, contact_supplier

urlpatterns = [
    path('show_interest/<int:post_id>/', views.show_interest, name='show_interest'),
    path('contact_supplier/<int:post_id>/', views.contact_supplier, name='contact_supplier'),
]
