# Generated by Django 3.0.7 on 2020-08-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_jumper'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jumper',
            name='jumper_Date_Of_Birth',
        ),
        migrations.AddField(
            model_name='jumper',
            name='jumper_Phone_Number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
