# Generated by Django 3.2.3 on 2021-11-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20211111_1641'),
        ('task', '0002_auto_20211111_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='_task_task_comments_+', to='comment.Comment'),
        ),
    ]
