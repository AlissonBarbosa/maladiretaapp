# Generated by Django 3.0 on 2020-09-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitations', '0002_solicitation_historic'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitation',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]