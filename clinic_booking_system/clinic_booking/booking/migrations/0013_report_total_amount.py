# Generated by Django 5.0.6 on 2024-08-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]
