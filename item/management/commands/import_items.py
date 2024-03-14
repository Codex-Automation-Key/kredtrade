import openpyxl
from django.core.management.base import BaseCommand
from pathlib import Path
from item.models import Item  # Replace 'myapp' with the actual app name
from market.models import Industry, Category
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist





class Command(BaseCommand):
    help = 'Import items from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The Excel file to import.')

    def handle(self, *args, **options):
        file_path = options['file_path']
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active

        for row in list(ws.iter_rows(min_row=2, values_only=True)):  # Assuming the first row is the header
            item_data = {
                'item_name': row[2],
                'item_description': row[3],
                'preferred_unit': row[7],
                'quantity': row[8],
                'quality_description': row[9],
                'price_per_unit': row[10],
                'available': row[11],
                'expiration_date': row[12],
                #'item_indusry' :row[1],
                #'item_category': row[2]
                # Add other fields as necessary
            }
            # You'll need to handle ForeignKey fields and ImageFields appropriately
            # For instance, you might need to fetch the related object like:
            industry = Industry.objects.get(industry_name=row[0])  # Assuming row[8] contains the industry name
            item_data['item_industry'] = industry

            try:
                category = Category.objects.get(hsn_6_digit=row[1])
                item_data['item_category'] = category
            except ObjectDoesNotExist:
                self.stdout.write(self.style.WARNING(f'Category with HSN 6-digit "{row[1]}" does not exist. Skipping item.'))
                continue  # Skip this item and go to the next

            
            created_by = User.objects.get(username= row[5])
            item_data['created_by'] = created_by
            # Similarly, you'll need to handle the created_by field which is a ForeignKey to the User model.
            # For image, you'll need to set a default or handle file paths if they're included in the Excel.

            Item.objects.create(**item_data)

        self.stdout.write(self.style.SUCCESS('Successfully imported items from "%s"' % file_path))
