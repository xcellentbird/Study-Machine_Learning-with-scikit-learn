# Generated by Django 3.2.5 on 2021-07-12 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='field1',
        ),
    ]