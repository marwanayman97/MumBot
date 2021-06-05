# Generated by Django 3.1.6 on 2021-06-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grad', '0007_auto_20210602_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='active_status',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='videosession',
            name='video_duration_in_minutes',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='videosession',
            name='video_price',
            field=models.FloatField(default=50),
        ),
        migrations.DeleteModel(
            name='SpecialistActiveStatus',
        ),
    ]
