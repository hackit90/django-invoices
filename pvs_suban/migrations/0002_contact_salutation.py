# Generated by Django 3.2.4 on 2021-06-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvs_suban', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='salutation',
            field=models.CharField(choices=[('herr', 'Herr'), ('frau', 'Frau'), ('familie', 'Familie')], default='frau', max_length=30),
        ),
    ]
