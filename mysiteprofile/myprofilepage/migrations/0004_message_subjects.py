# Generated by Django 4.1.3 on 2022-11-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofilepage', '0003_alter_message_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subjects',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
