# Generated by Django 3.2.5 on 2021-08-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20210814_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='blogging', max_length=255),
        ),
    ]
