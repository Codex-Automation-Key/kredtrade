from django.contrib import admin
from .models import Post, Industry, Category, Sector, Intent

admin.site.register(Post)
admin.site.register(Industry)
admin.site.register(Category)
admin.site.register(Sector)
admin.site.register(Intent)