# Generated by Django 3.0 on 2020-08-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20200831_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]