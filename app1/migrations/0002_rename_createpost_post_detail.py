# Generated by Django 5.0 on 2024-09-25 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreatePost',
            new_name='Post_detail',
        ),
    ]
