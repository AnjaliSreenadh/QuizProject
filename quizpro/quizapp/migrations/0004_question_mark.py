# Generated by Django 5.0.4 on 2024-04-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_question_delete_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='mark',
            field=models.IntegerField(default=0),
        ),
    ]
