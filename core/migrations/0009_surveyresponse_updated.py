# Generated by Django 2.1.1 on 2018-09-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180927_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresponse',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]