# Generated by Django 3.2.3 on 2021-11-06 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Ошибка', max_length=64, verbose_name='Тип ошибки')),
            ],
            options={
                'verbose_name_plural': 'Тип ошибки',
            },
        ),
        migrations.AddField(
            model_name='bug',
            name='bug_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bug_tracker.bug_type'),
        ),
    ]
