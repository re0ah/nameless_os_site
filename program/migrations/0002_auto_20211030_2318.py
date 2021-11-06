# Generated by Django 3.2.3 on 2021-10-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='source',
            field=models.URLField(default='https://github.com/re0ah/nameless-OS16'),
        ),
        migrations.AlterField(
            model_name='program',
            name='active',
            field=models.BooleanField(blank=True),
        ),
    ]
