# Generated by Django 3.1.6 on 2021-06-01 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grad', '0004_auto_20210601_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_day', models.CharField(max_length=20)),
                ('slot_start_time', models.TimeField()),
                ('slot_end_time', models.TimeField()),
                ('booked', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialistActiveStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='specialist_active_status',
        ),
        migrations.DeleteModel(
            name='Schedules',
        ),
        migrations.AddField(
            model_name='specialistactivestatus',
            name='specilist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grad.specialist'),
        ),
        migrations.AddField(
            model_name='slots',
            name='schedule_specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grad.specialist'),
        ),
    ]
