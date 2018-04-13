# Generated by Django 2.0.3 on 2018-04-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20180401_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='predecessor',
            field=models.ManyToManyField(blank=True, null=True, related_name='_task_predecessor_+', to='project.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='successor',
            field=models.ManyToManyField(blank=True, null=True, related_name='_task_successor_+', to='project.Task'),
        ),
    ]
