# Generated by Django 2.2.7 on 2019-12-20 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0023_auto_20191219_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='test',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
