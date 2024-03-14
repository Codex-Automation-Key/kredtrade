from django.db import models
from django.contrib.auth.models import User
from PIL import Image   
from market.models import Intent, Sector
import datetime

def year_choices():
    return [(r,r) for r in range(1980, datetime.date.today().year+1)]

# Helper function to get the current year
def current_year():
    return datetime.date.today().year

class State(models.Model):
    
    STATE_CHOICES = [
        ('TRIPURA', 'Tripura'),
        ('UTTAR_PRADESH', 'Uttar Pradesh'),
        ('GUJARAT', 'Gujarat'),
        ('MIZORAM', 'Mizoram'),
        ('RAJASTHAN', 'Rajasthan'),
        ('KERALA', 'Kerala'),
        ('MAHARASHTRA', 'Maharashtra'),
        ('UTTARANCHAL', 'Uttaranchal'),
        ('HARYANA', 'Haryana'),
        ('MADHYA_PRADESH', 'Madhya Pradesh'),
        ('PUNJAB', 'Punjab'),
        ('HIMACHAL_PRADESH', 'Himachal Pradesh'),
        ('KARNATAKA', 'Karnataka'),
        ('ORISSA', 'Orissa'),
        ('CHHATTISGARH', 'Chhattisgarh'),
        ('BIHAR', 'Bihar'),
        ('TAMIL_NADU', 'Tamil Nadu'),
        ('UNION_TERRITORY_of_DADRA_&_NAGAR_HAVELI', 'Union Territory Of Dadra & Nagar Haveli'),
        ('WEST_BENGAL', 'West Bengal'),
        ('ASSAM', 'Assam'),
        ('SIKKIM', 'Sikkim'),
        ('NEW_DELHI', 'New Delhi'),
        ('GOA', 'Goa'),
        ('NCR', 'Ncr'),
        ('JAMMU_&_KASHMIR', 'Jammu & Kashmir'),
        ('ANDHRA_PRADESH', 'Andhra Pradesh'),
        ('MANIPUR', 'Manipur'),
        ('JHARKHAND', 'Jharkhand'),
        ('UTTARAKHAND', 'Uttarakhand'),
        ('NORTH_SIKKIM', 'North Sikkim'),
        ('UNION_TERRITORY_OF_LAKSHADWEEP', 'Union Territory Of Lakshadweep'),
        ('NEPAL', 'Nepal'),
        ('DELHI', 'Delhi'),
        ('WEST_SIKKIM', 'West Sikkim'),
        ('ANDAMAN_&_NICOBAR_ISLANDS', 'Andaman & Nicobar Islands'),
        ('MEGHALAYA', 'Meghalaya')
    ]
    name = models.CharField(max_length=100, choices=STATE_CHOICES, default='NCR')
    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, related_name='cities', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    COUNTRY_CHOICES = [
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
    
    STATE_CHOICES = [
        ('TRIPURA', 'Tripura'),
        ('UTTAR_PRADESH', 'Uttar Pradesh'),
        ('GUJARAT', 'Gujarat'),
        ('MIZORAM', 'Mizoram'),
        ('RAJASTHAN', 'Rajasthan'),
        ('KERALA', 'Kerala'),
        ('MAHARASHTRA', 'Maharashtra'),
        ('UTTARANCHAL', 'Uttaranchal'),
        ('HARYANA', 'Haryana'),
        ('MADHYA_PRADESH', 'Madhya Pradesh'),
        ('PUNJAB', 'Punjab'),
        ('HIMACHAL_PRADESH', 'Himachal Pradesh'),
        ('KARNATAKA', 'Karnataka'),
        ('ORISSA', 'Orissa'),
        ('CHHATTISGARH', 'Chhattisgarh'),
        ('BIHAR', 'Bihar'),
        ('TAMIL_NADU', 'Tamil Nadu'),
        ('UNION_TERRITORY_of_DADRA_&_NAGAR_HAVELI', 'Union Territory Of Dadra & Nagar Haveli'),
        ('WEST_BENGAL', 'West Bengal'),
        ('ASSAM', 'Assam'),
        ('SIKKIM', 'Sikkim'),
        ('NEW_DELHI', 'New Delhi'),
        ('GOA', 'Goa'),
        ('NCR', 'Ncr'),
        ('JAMMU_&_KASHMIR', 'Jammu & Kashmir'),
        ('ANDHRA_PRADESH', 'Andhra Pradesh'),
        ('MANIPUR', 'Manipur'),
        ('JHARKHAND', 'Jharkhand'),
        ('UTTARAKHAND', 'Uttarakhand'),
        ('NORTH_SIKKIM', 'North Sikkim'),
        ('UNION_TERRITORY_OF_LAKSHADWEEP', 'Union Territory Of Lakshadweep'),
        ('NEPAL', 'Nepal'),
        ('DELHI', 'Delhi'),
        ('WEST_SIKKIM', 'West Sikkim'),
        ('ANDAMAN_&_NICOBAR_ISLANDS', 'Andaman & Nicobar Islands'),
        ('MEGHALAYA', 'Meghalaya'),
    ]
    EMPLOYEE_CHOICES = [
        ('1-10', '1-10'),
        ('11-50', '11-50'),
        ('51-100', '51-100'),
        ('100+', '100+'),
    ]
    TURNOVER_CHOICES = [
        ('<5Cr', 'Less Than 5 Crore'),
        ('5Cr-50Cr', 'From 5 Crore to 50 Crore'),
        ('50Cr-250Cr', 'From 50 Crore to 250 Crore'),
        ('250Cr+', 'More Than 250 Crore')
    ]
    STATUS_CHOICES = [
        ('Proprietorship', 'Proprietorship'),
        ('Partnership', 'Partnership'),
        ('LLP', 'Limited Liability Partnership'),
        ('PvtLtd', 'Private Limited'),
        ('PubLtd', 'Public Limited'),
        ('Gov', 'Government Undertaking'),
        ('NPO', 'NPO/AOP/SHG/Cooperative Societies/Trust'),
    ]
    NATURE_CHOICES = [
        ('MANUFACTURER', 'MANUFACTURER'),
        ('TRADER', 'TRADER'),
        ('MANUFACTURER-EXPORTER', 'MANUFACTURER-EXPORTER'),
        ('EXPORTER', 'EXPORTER'),
        ('IMPORTER', 'IMPORTER'),
        ('MANUFACTURER-EXPORTER-IMPORTER', 'MANUFACTURER-EXPORTER-IMPORTER')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')
    
    #Company Details
    company = models.TextField(default= 'company', max_length=50)
    address = models.TextField(default= 'N/A', max_length=100)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES, default='India')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='profile_state',  null=True, blank=True)
    
    est = models.IntegerField('Establishment Year', choices=year_choices(), default=current_year)
    nature = models.TextField(max_length=50, choices=NATURE_CHOICES, default='trade')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Proprietorship')
    description = models.TextField(default='Business Description')
    turnover = models.CharField(max_length=20, choices=TURNOVER_CHOICES, default='<1M')
    employee = models.CharField(max_length=20, choices=EMPLOYEE_CHOICES, default='1-5')
    
    #Personnel Details
    promotor_name = models.TextField(max_length=50, default='N/A')
    promotror_mail = models.EmailField(default='promotor@mail.com')
    promotor_mob = models.TextField(default = '--', max_length=10 )
    auth_name = models.TextField(max_length=50, default='N/A')
    auth_mail = models.EmailField(default='auth@mail.com')
    auth_mob = models.TextField(default = '--', max_length=10 )
    
    #KYC Documents
    gst_no = models.TextField(default='N/A', max_length=20, null=True)
    pan_no = models.TextField(default='N/A', max_length=20, null=True)
    udyam_no = models.TextField(default='N/A', max_length=20, null=True)
    iec_no = models.TextField(default='N/A', max_length=20, null=True)
    gst = models.FileField(upload_to='documents/gst/', null=True, blank=True)
    pan = models.FileField(upload_to='documents/pan/', null=True, blank=True)
    udyam = models.FileField(upload_to='documents/udyam/', null=True, blank=True)
    iec = models.FileField(upload_to='documents/iec/', null=True, blank=True)
    
    #Factory Details
    factoryaddress = models.TextField(default='N/A', max_length=50, null=True)
    factorydesc = models.TextField(default='N/A', max_length=50, null=True)
    factorytype = models.TextField(default='N/A', max_length=50, null=True)
    factorylabors = models.IntegerField(default=0, null=True, blank=True)
    
    #
    



    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class RegistrationCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates")
    certificate_name = models.CharField(max_length=255)
    certificate_file = models.FileField(upload_to='documents/certificates/')
    issued_by = models.CharField(max_length=255, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    valid_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.certificate_name} for {self.user.username}"
