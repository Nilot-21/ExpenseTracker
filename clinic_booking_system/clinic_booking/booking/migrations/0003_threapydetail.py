# Generated by Django 5.0.6 on 2024-07-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_doctorrefer'),
    ]

    operations = [
        migrations.CreateModel(
            name='threapydetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp_beforebreakfast', models.IntegerField()),
                ('bp_afterbreakfast', models.IntegerField()),
                ('doctor_suggestion', models.TextField()),
            ],
        ),
    ]
