# Generated by Django 3.2.4 on 2021-06-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvs_suban', '0015_alter_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoiceposition',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]