# Generated by Django 2.0.3 on 2018-04-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskrel',
            name='predecessors',
        ),
        migrations.RemoveField(
            model_name='taskrel',
            name='successor',
        ),
        migrations.AddField(
            model_name='task',
            name='optimistic_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='pessimistic_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='predecessor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='realistic_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.DeleteModel(
            name='TaskRel',
        ),
    ]
