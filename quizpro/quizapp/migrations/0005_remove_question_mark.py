# Generated by Django 5.0.4 on 2024-04-18 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_question_mark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='mark',
        ),
    ]