# Generated by Django 2.1.1 on 2018-09-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_surveyresponse_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='iso',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
