# Generated by Django 4.1.1 on 2022-10-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_problems_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='subject',
            field=models.CharField(default='', max_length=200),
        ),
    ]
