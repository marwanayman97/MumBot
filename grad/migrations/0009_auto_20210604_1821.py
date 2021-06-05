# Generated by Django 3.1.6 on 2021-06-04 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grad', '0008_auto_20210602_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videosession',
            name='specialist_id',
        ),
        migrations.RemoveField(
            model_name='videosession',
            name='video_date',
        ),
        migrations.RemoveField(
            model_name='videosession',
            name='video_end_time',
        ),
        migrations.RemoveField(
            model_name='videosession',
            name='video_start_time',
        ),
        migrations.AddField(
            model_name='videosession',
            name='video_slot',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, to='grad.slots'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_start_time',
            field=models.TimeField(),
        ),
    ]
