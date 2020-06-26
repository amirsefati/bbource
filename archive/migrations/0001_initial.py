# Generated by Django 3.0.7 on 2020-06-26 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agriculture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=250)),
                ('api', models.CharField(max_length=250)),
                ('history', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='basic_metal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='coal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='comm_devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='elec_computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='electrical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='metal_ores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='metal_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='multidisciplinary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='oil_gas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='other_mines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pet_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='plastic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='printz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='textiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='wood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('data', models.TextField()),
            ],
        ),
    ]