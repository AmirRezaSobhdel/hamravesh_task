# Generated by Django 4.0.4 on 2022-12-02 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapp', '0005_container_logs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='docker_container_internal_id',
        ),
    ]
