# Generated by Django 2.1.4 on 2019-01-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0008_auto_20190105_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rounds',
            name='Date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
