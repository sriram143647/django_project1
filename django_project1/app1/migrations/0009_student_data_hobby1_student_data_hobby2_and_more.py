# Generated by Django 4.0.4 on 2022-06-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_student_data_add2_student_data_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='hobby1',
            field=models.BooleanField(default=False, verbose_name='Reading Books'),
        ),
        migrations.AddField(
            model_name='student_data',
            name='hobby2',
            field=models.BooleanField(default=False, verbose_name='Travelling'),
        ),
        migrations.AddField(
            model_name='student_data',
            name='hobby3',
            field=models.BooleanField(default=False, verbose_name='Listening Music'),
        ),
        migrations.AddField(
            model_name='student_data',
            name='hobby4',
            field=models.BooleanField(default=False, verbose_name='Coding'),
        ),
        migrations.AddField(
            model_name='student_data',
            name='hobby5',
            field=models.BooleanField(default=False, verbose_name='Sports'),
        ),
    ]
