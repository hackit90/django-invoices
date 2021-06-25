# Generated by Django 3.2.4 on 2021-06-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvs_suban', '0004_alter_country_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256)),
                ('condition', models.CharField(max_length=256)),
                ('due', models.DateField()),
                ('date', models.DateField()),
            ],
        ),
    ]
