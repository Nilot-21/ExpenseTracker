# Generated by Django 5.0.6 on 2024-08-03 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_remove_fee_total_amount_report_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='fee',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]
