# Generated by Django 3.0 on 2020-08-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
