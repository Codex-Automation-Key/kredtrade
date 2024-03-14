from django.db import models
from market.models import Industry, Category
from django.contrib.auth.models import User
from PIL import Image   


class Item(models.Model):
    UNIT_CHOICES = [
    ('KG', 'Kilogram'),
    ('LBS', 'Pounds'),
    ('PCS', 'Pieces'),
    ('L', 'Liters'),
    ('M', 'Meters'),
    ('CM', 'Centimeters'),
    ('MM', 'Millimeters'),
    ('SQM', 'Square Meters'),
    ('CU', 'Cubic Meters'),
    ('G', 'Grams'),
    ('MG', 'Milligrams'),
    ('OZ', 'Ounces'),
    ('FL OZ', 'Fluid Ounces'),
    ('GAL', 'Gallons'),
    ('QT', 'Quarts'),
    ('PT', 'Pints'),
    ('YD', 'Yards'),
    ('IN', 'Inches'),
]
    
    item_industry = models.ForeignKey(Industry, related_name='items', on_delete=models.CASCADE)
    item_category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True, default='168.jpg')
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # New fields
    preferred_unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='PCS')
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Supports decimal quantities
    quality_description = models.TextField(blank=True, null=True)
    
    # Additional fields that might be relevant
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available = models.BooleanField(default=True)  # Indicates if the item is currently available
    expiration_date = models.DateField(null=True, blank=True, help_text="Best used before date for perishable items")  # Useful for perishable goods

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.item_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize image
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
