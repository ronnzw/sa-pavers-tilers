# Generated by Django 2.0 on 2019-04-26 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emai',
            new_name='email',
        ),
    ]
