# Generated by Django 2.1.1 on 2018-09-27 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_surveycampaign_instructions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyresponse',
            name='response',
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.SurveyCampaign'),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.TableColumn'),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='row',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.TableRow'),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.TableSpecification'),
        ),
    ]
