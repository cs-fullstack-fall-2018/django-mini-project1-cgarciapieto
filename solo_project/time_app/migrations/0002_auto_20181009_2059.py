# Generated by Django 2.0.6 on 2018-10-09 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hours',
            field=models.IntegerField(),
        ),
    ]