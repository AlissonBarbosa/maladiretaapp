# Generated by Django 3.0 on 2020-09-04 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0005_auto_20200824_1942'),
        ('positions', '0003_auto_20200801_0218'),
        ('authorities', '0009_auto_20200831_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authoritie',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='institutions.Institution'),
        ),
        migrations.AlterField(
            model_name='authoritie',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='positions.Position'),
        ),
    ]
