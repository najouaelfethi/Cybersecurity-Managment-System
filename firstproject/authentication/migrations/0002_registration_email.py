# Generated by Django 4.2.1 on 2023-05-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.CharField(default='email', max_length=50),
        ),
    ]
