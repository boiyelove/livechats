# Generated by Django 3.1.7 on 2021-03-15 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatRoom',
            new_name='Thread',
        ),
    ]
