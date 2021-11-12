# Generated by Django 3.2.3 on 2021-11-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='answer',
        ),
        migrations.AddField(
            model_name='comment',
            name='answer',
            field=models.ManyToManyField(blank=True, null=True, related_name='_comment_comment_answer_+', to='comment.Comment'),
        ),
    ]
