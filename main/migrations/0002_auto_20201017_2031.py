# Generated by Django 3.1.2 on 2020-10-17 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='username',
            new_name='user',
        ),
    ]
