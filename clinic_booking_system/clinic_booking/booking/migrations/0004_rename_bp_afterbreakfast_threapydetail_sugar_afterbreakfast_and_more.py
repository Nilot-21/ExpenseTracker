# Generated by Django 5.0.6 on 2024-07-31 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_threapydetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='threapydetail',
            old_name='bp_afterbreakfast',
            new_name='sugar_afterbreakfast',
        ),
        migrations.RenameField(
            model_name='threapydetail',
            old_name='bp_beforebreakfast',
            new_name='sugar_beforebreakfast',
        ),
    ]
