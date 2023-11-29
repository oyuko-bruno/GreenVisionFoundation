# Generated by Django 4.2.7 on 2023-11-27 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonorList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6, null=True)),
                ('tree_donate', models.CharField(blank=True, choices=[('100', '100'), ('300', '300'), ('500', '500'), ('700', '700'), ('900', '900'), ('1100', '1100'), ('2000', '2000'), ('10000', '10000')], max_length=100, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('occupation', models.CharField(blank=True, max_length=10, null=True)),
                ('home_address', models.TextField(blank=True, null=True)),
                ('last_donate_date', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]