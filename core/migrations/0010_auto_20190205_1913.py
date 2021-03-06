# Generated by Django 2.1.5 on 2019-02-05 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_surveyresponse_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablerow',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Organisation'),
        ),
        migrations.AddField(
            model_name='tablespecification',
            name='allow_user_rows',
            field=models.BooleanField(default=False),
        ),
    ]
