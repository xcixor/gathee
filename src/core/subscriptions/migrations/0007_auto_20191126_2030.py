# Generated by Django 2.2.7 on 2019-11-26 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_auto_20191126_2023'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='premiumvideodemo',
            unique_together={('demo_video', 'premium_video')},
        ),
    ]
