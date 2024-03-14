from django.urls import path
from . import views

app_name = 'item'


urlpatterns = [
    path('item/<int:pk>/', views.detail, name = 'detail'),
    path('item/new/', views.newitem, name = 'new-item'),
    path('<int:pk>/delete/', views.delete, name= 'delete-item'),
    path('<int:pk>/edit/', views.edititem, name= 'edit-item'),
    path('items/',views.items, name = 'items' )
]