# Generated by Django 4.1 on 2022-09-01 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_company_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]