# Generated by Django 3.1 on 2020-08-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
