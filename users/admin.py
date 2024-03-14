from django.contrib import admin
from .models import Profile, RegistrationCertificate, City, State

admin.site.register(Profile)
admin.site.register(RegistrationCertificate)
admin.site.register(City)
admin.site.register(State)
