# Generated by Django 3.1.3 on 2020-11-19 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=512, verbose_name='organization_name'),
        ),
    ]
