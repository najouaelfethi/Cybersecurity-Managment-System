# Generated by Django 4.2 on 2023-06-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_profil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=50)),
                ('response', models.CharField(max_length=50)),
                ('maturite', models.CharField(max_length=50)),
            ],
        ),
    ]
