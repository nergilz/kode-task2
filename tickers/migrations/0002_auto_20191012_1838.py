# Generated by Django 2.2.6 on 2019-10-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='symbol',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
