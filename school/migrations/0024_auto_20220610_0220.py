# Generated by Django 3.0.5 on 2022-06-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0023_book_issuedbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='branch',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='enrollment',
            field=models.CharField(default=False, max_length=40),
        ),
    ]
