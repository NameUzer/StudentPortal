# Generated by Django 3.0.5 on 2022-06-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='RecieverNo',
            field=models.IntegerField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='message',
            name='senderNo',
            field=models.IntegerField(default=0, max_length=15),
        ),
    ]
