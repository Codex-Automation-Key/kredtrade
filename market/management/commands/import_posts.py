from django.core.management.base import BaseCommand
from market.models import Post, Industry, Category, Intent, User
from django.utils.dateparse import parse_datetime
import datetime

import openpyxl

class Command(BaseCommand):
    help = 'Imports posts from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The Excel file to import posts from')

    def handle(self, *args, **options):
        file_path = options['file_path']
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            title, content, date_posted_str, author_username, image_path, industry_name,  intent_name, target_country, source_country, *_ = row
            date_posted = row[2]

            # Check if date_posted_str is already a datetime object
            if isinstance(date_posted_str, datetime.datetime):
                date_posted = date_posted_str
            elif isinstance(date_posted_str, str):
                # If it's a string, parse it
                date_posted = parse_datetime(date_posted_str)
            else:
                # Handle cases where date_posted_str is neither datetime nor string (e.g., None or incorrect format)
                self.stdout.write(self.style.WARNING(f'Skipping row due to invalid date format: {date_posted_str}'))
                continue  # Skip this row or handle as needed


            # Handle related objects
            industry, _ = Industry.objects.get_or_create(industry_name=industry_name)
            #category, _ = Category.objects.get_or_create(category_name=category_name, industry=industry)
            intent, _ = Intent.objects.get_or_create(name=intent_name)
            author, _ = User.objects.get_or_create(username=author_username)  # Assuming User model exists and usernames are unique

            Post.objects.create(
                title=title,
                content=content,
                date_posted=date_posted,
                author=author,
                image=image_path,  # Assuming Post model has an 'image' field for image_path
                post_industry=industry,
                #category=category,
                intent=intent,
                target_country=target_country,
                source_country=source_country,
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported posts from "%s"' % file_path))
