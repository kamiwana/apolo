# Generated by Django 2.0.6 on 2018-09-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0005_auto_20180629_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록일'),
        ),
    ]
