# Generated by Django 5.0.6 on 2024-07-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Notes', '0002_delete_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='test2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Text', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]