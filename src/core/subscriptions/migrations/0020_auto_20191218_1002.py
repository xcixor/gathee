# Generated by Django 2.2.7 on 2019-12-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0019_auto_20191218_0617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='premiumvideodemo',
            options={'verbose_name_plural': 'Associate A video demo with its Course'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_number',
            field=models.IntegerField(default=1, help_text='The position of the lesson in the course', unique=True),
            preserve_default=False,
        ),
    ]
