from django.db import models
from django.conf import settings

class UserInterest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('market.Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class SupplierMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    post = models.ForeignKey('market.Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
