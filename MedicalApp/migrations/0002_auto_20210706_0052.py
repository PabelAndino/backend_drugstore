# Generated by Django 3.2.5 on 2021-07-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='buy_price',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='sell_price',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
