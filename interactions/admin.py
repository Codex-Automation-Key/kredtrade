from django.contrib import admin
from .models import UserInterest, SupplierMessage, ContactMessage


admin.site.register(UserInterest)
admin.site.register(SupplierMessage)
admin.site.register(ContactMessage)