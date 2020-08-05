# Generated by Django 3.0 on 2020-08-04 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leadership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('initials', models.CharField(max_length=25)),
                ('number', models.IntegerField()),
                ('union', models.CharField(blank=True, max_length=350, null=True)),
                ('presidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadership.Leadership')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
