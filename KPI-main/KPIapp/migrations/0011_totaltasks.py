# Generated by Django 4.2.15 on 2024-08-25 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KPIapp', '0010_alter_tasks_boss_alter_tasks_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_tasks', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_total', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
