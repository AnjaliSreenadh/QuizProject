# Generated by Django 5.0.4 on 2024-04-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='mark',
            field=models.IntegerField(default=0),
        ),
    ]
