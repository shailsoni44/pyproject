# Generated by Django 2.1.5 on 2020-05-31 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20200530_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('repeat_email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Register',
            },
        ),
    ]