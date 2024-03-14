from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from market.models import Category, Industry
import openpyxl
import os

class Command(BaseCommand):
    help = 'Import categories from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file containing category data')

    def handle(self, *args, **options):
        excel_file_path = options['excel_file']
        excel_dir = os.path.dirname(excel_file_path)

        try:
            wb = openpyxl.load_workbook(excel_file_path)
            sheet = wb.active
            for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming first row is headers
                industry_name, category_name, category_desc, hsn_6_digit, image_path = row
                
                # Get or create the Industry instance
                industry, _ = Industry.objects.get_or_create(
                    industry_name=industry_name
                )
                
                # Create the Category instance
                category, created = Category.objects.get_or_create(
                    industry=industry,
                    category_name=category_name,
                    defaults={
                        'category_desc': category_desc,
                        'hsn_6_digit': hsn_6_digit
                    }
                )

                # If the category was created and an image path is provided
                if created and image_path:
                    full_image_path = os.path.join(excel_dir, image_path)
                    if os.path.exists(full_image_path):
                        with open(full_image_path, 'rb') as image_file:
                            django_file = File(image_file)
                            category.category_img.save(os.path.basename(image_path), django_file, save=True)
                    else:
                        self.stdout.write(self.style.WARNING(f'Image file not found: {full_image_path}'))

            self.stdout.write(self.style.SUCCESS('Successfully imported categories from Excel file.'))
        except openpyxl.utils.exceptions.InvalidFileException:
            raise CommandError('The Excel file could not be opened. Please make sure it is an .xlsx file.')
        except Exception as e:
            raise CommandError(f'Error importing categories: {e}')
