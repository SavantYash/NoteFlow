# Generated by Django 5.0.6 on 2024-07-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='test2',
        ),
    ]