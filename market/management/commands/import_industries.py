from django.core.management.base import BaseCommand, CommandError
from market.models import Industry, Sector
import openpyxl  # Use xlrd for .xls files

class Command(BaseCommand):
    help = 'Imports industries from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file containing industry data')

    def handle(self, *args, **options):
        excel_file_path = options['excel_file']
        try:
            wb = openpyxl.load_workbook(excel_file_path)
            sheet = wb.active
            for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming the first row is headers
                sector, industry_name, industry_desc, hsn_2_digit = row
                Industry.objects.get_or_create(
                    industry_name=industry_name,
                    defaults={'industry_desc': industry_desc, 'hsn_2_digit': hsn_2_digit, 'sector':None}
                )
            self.stdout.write(self.style.SUCCESS('Successfully imported industries from "%s"' % excel_file_path))
        except Exception as e:
            raise CommandError('Error importing industries: %s' % e)
