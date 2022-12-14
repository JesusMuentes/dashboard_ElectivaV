# Generated by Django 4.0.4 on 2022-11-06 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tornado', '0004_auto_20190430_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tornado',
            name='date',
        ),
        migrations.RemoveField(
            model_name='tornado',
            name='distance_covered',
        ),
        migrations.RemoveField(
            model_name='tornado',
            name='end_location',
        ),
        migrations.RemoveField(
            model_name='tornado',
            name='fujita_scale_rating',
        ),
        migrations.RemoveField(
            model_name='tornado',
            name='rotation',
        ),
        migrations.RemoveField(
            model_name='tornado',
            name='start_location',
        ),
        migrations.RemoveField(
            model_name='tornado',
            name='wind_speed',
        ),
        migrations.AddField(
            model_name='tornado',
            name='tnaño1',
            field=models.CharField(default='2019', max_length=50),
        ),
        migrations.AddField(
            model_name='tornado',
            name='tnaño2',
            field=models.CharField(default='2020', max_length=50),
        ),
        migrations.AddField(
            model_name='tornado',
            name='tnaño3',
            field=models.CharField(default='2021', max_length=50),
        ),
        migrations.AddField(
            model_name='tornado',
            name='tncategoria',
            field=models.CharField(default='Suicidios', max_length=50),
        ),
        migrations.AddField(
            model_name='tornado',
            name='tncifra1',
            field=models.CharField(default='688', max_length=50),
        ),
        migrations.AddField(
            model_name='tornado',
            name='tncifra2',
            field=models.CharField(default='347', max_length=50),
        ),
        migrations.AddField(
            model_name='tornado',
            name='tncifra3',
            field=models.CharField(default='417', max_length=50),
        ),
    ]
