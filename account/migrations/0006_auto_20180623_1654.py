# Generated by Django 2.0.6 on 2018-06-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_user_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_key',
            field=models.CharField(max_length=170, unique=True),
        ),
    ]