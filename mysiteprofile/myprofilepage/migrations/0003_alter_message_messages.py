# Generated by Django 4.1.3 on 2022-11-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofilepage', '0002_alter_message_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='messages',
            field=models.TextField(max_length=2000),
        ),
    ]
