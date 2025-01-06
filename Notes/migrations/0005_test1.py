# Generated by Django 5.0.6 on 2024-07-27 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0004_test_delete_test2'),
    ]

    operations = [
        migrations.CreateModel(
            name='test1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('password', models.CharField(max_length=20)),
                ('User_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.test')),
            ],
        ),
    ]