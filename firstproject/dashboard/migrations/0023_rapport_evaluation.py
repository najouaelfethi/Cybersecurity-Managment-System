# Generated by Django 4.2 on 2023-06-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_rapport'),
    ]

    operations = [
        migrations.AddField(
            model_name='rapport',
            name='evaluation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
