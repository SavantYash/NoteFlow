# Generated by Django 5.0.6 on 2024-07-28 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0009_remove_test1_user_id_remove_test1_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test1',
            old_name='user_id',
            new_name='user',
        ),
    ]