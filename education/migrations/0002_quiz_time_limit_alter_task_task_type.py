# Generated by Django 5.1.2 on 2024-10-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='time_limit',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('word_input', 'Word Input'), ('number_input', 'Number Input'), ('sentence_fill', 'Fill in the Blank'), ('multiple_choice', 'Multiple Choice'), ('multiplication', 'Multiplication')], max_length=20),
        ),
    ]
