# Generated by Django 3.0 on 2020-07-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0007_auto_20200730_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='authoritie',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='authoritie',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
