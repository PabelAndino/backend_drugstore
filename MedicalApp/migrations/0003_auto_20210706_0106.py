# Generated by Django 3.2.5 on 2021-07-06 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalApp', '0002_auto_20210706_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='expire_date',
            field=models.DateField(),
        ),
    ]
