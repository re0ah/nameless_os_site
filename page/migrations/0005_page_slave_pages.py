# Generated by Django 3.2.3 on 2021-10-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_rename_subpage_page_master_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slave_pages',
            field=models.ManyToManyField(blank=True, null=True, related_name='_page_page_slave_pages_+', to='page.Page'),
        ),
    ]
