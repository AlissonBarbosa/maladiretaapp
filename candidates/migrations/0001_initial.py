# Generated by Django 3.0 on 2020-08-05 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parties', '0002_auto_20200805_2020'),
        ('positions', '0003_auto_20200801_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('union', models.CharField(blank=True, max_length=350, null=True)),
                ('votes', models.IntegerField(blank=True, null=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parties.Party')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positions.Position')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]