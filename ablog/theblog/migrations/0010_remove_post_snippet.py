# Generated by Django 3.2.7 on 2021-09-14 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_alter_post_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
    ]
