# Generated by Django 3.0 on 2020-08-07 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leadership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('birth', models.DateField(blank=True, null=True)),
                ('nickname', models.CharField(blank=True, max_length=80, null=True)),
                ('reference', models.CharField(blank=True, max_length=180, null=True)),
                ('city', models.CharField(blank=True, max_length=80, null=True)),
                ('street', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('complement', models.CharField(blank=True, max_length=30, null=True)),
                ('cep', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=60, null=True)),
                ('rg', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('cpf', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=25, null=True)),
                ('phone_home', models.CharField(blank=True, max_length=25, null=True)),
                ('subscription', models.CharField(blank=True, max_length=30, null=True)),
                ('zone', models.CharField(blank=True, max_length=30, null=True)),
                ('section', models.CharField(blank=True, max_length=30, null=True)),
                ('profession', models.CharField(blank=True, max_length=80, null=True)),
                ('leadership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leadership.Leadership')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]