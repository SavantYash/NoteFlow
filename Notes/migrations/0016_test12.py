# Generated by Django 5.0.6 on 2024-08-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0015_remove_test_u_id_test_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='test12',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]