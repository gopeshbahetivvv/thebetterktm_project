# Generated by Django 4.1.1 on 2022-11-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_user_userip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userip',
            field=models.JSONField(default=str),
        ),
    ]