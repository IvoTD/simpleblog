# Generated by Django 3.2.7 on 2021-09-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_auto_20210919_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkdin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
