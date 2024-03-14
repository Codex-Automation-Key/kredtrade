from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image   

class Sector(models.Model):
    sector_name = models.CharField(max_length=100)
    sector_desc = models.TextField()

    def __str__(self):
        return self.sector_name

class Industry(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='industries',null=True, blank=True)  # Link to Sector
    industry_name = models.CharField(max_length=100)
    industry_desc = models.TextField()
    hsn_2_digit = models.CharField(max_length=2)
    industry_img = models.ImageField(default='kreditem.png', upload_to='industry_pics')

    def __str__(self):
        return self.industry_name

class Category(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='categories')
    category_name = models.CharField(max_length=100)
    category_desc = models.TextField()
    hsn_6_digit = models.CharField(max_length=6)
    category_img = models.ImageField(default='kreditem.png', upload_to = 'category_pics')

    @property
    def hsn_2_digit(self):
        return self.industry.hsn_2_digit

    def __str__(self):
        return self.hsn_6_digit

class Intent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='kreditem.png', upload_to = 'post_pics')
    
    post_industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    post_category_hsn = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True) 
    
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    COUNTRY_CHOICES = [
        ('World wide', 'World Wide'), 
        ('United States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('France', 'France'),
        ('Germany', 'Germany'),
        ('Afghanistan', 'Afghanistan'),
        ('Armenia', 'Armenia'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Bhutan', 'Bhutan'),
        ('Brunei', 'Brunei'),
        ('Cambodia', 'Cambodia'),
        ('China', 'China'),
        ('Cyprus', 'Cyprus'),
        ('Georgia', 'Georgia'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Israel', 'Israel'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Lebanon', 'Lebanon'),
        ('Macao', 'Macao'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mongolia', 'Mongolia'),
        ('Myanmar', 'Myanmar'),
        ('Nepal', 'Nepal'),
        ('North Korea', 'North Korea'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palestine', 'Palestine'),
        ('Philippines', 'Philippines'),
        ('Qatar', 'Qatar'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Singapore', 'Singapore'),
        ('South Korea', 'South Korea'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Thailand', 'Thailand'),
        ('Timor-Leste', 'Timor-Leste'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        # Add more countries as needed
    ]
    target_country = models.CharField(max_length=255, choices=COUNTRY_CHOICES, default='India')
    source_country = models.CharField(max_length=255, choices=COUNTRY_CHOICES, default='India')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 700 or img.width >700:
            output_size = (700, 700)
            img.thumbnail(output_size)
            img.save(self.image.path)
