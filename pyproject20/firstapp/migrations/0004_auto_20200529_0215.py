# Generated by Django 2.1.5 on 2020-05-29 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_session_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='id',
        ),
        migrations.AlterField(
            model_name='session',
            name='session',
            field=models.CharField(max_length=40, primary_key=True, serialize=False, unique=True),
        ),
    ]
