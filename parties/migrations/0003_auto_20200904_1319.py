# Generated by Django 3.0 on 2020-09-04 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leadership', '0008_auto_20200903_0125'),
        ('parties', '0002_auto_20200805_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='leadership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leadership.Leadership'),
        ),
    ]
