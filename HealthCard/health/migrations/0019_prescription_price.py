# Generated by Django 3.1.4 on 2021-01-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0018_billing_record_medical_record_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
