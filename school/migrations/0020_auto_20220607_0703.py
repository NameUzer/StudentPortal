# Generated by Django 3.0.5 on 2022-06-06 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0019_auto_20220606_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='RecieverNo',
        ),
        migrations.RemoveField(
            model_name='message',
            name='senderNo',
        ),
    ]
