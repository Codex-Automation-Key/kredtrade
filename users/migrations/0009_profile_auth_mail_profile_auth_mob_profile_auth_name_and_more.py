# Generated by Django 5.0 on 2024-02-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_profile_promotror_mail"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="auth_mail",
            field=models.EmailField(default="auth@mail.com", max_length=254),
        ),
        migrations.AddField(
            model_name="profile",
            name="auth_mob",
            field=models.TextField(default="--", max_length=10),
        ),
        migrations.AddField(
            model_name="profile",
            name="auth_name",
            field=models.TextField(default="N/A", max_length=50),
        ),
        migrations.AddField(
            model_name="profile",
            name="factoryaddress",
            field=models.TextField(default="N/A", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="factorydesc",
            field=models.TextField(default="N/A", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="factorylabors",
            field=models.IntegerField(default="1"),
        ),
        migrations.AddField(
            model_name="profile",
            name="factorytype",
            field=models.TextField(default="N/A", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="fssai",
            field=models.TextField(default="N/A", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="gst",
            field=models.TextField(default="N/A", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="iec",
            field=models.TextField(default="N/A", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="promotor_mob",
            field=models.TextField(default="--", max_length=10),
        ),
        migrations.AddField(
            model_name="profile",
            name="udyam",
            field=models.TextField(default="N/A", max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="turnover",
            field=models.TextField(default="00", max_length=20),
        ),
    ]
