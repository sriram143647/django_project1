# Generated by Django 4.0.4 on 2022-06-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_student_data_hobby1_student_data_hobby2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='hobby1',
            field=models.BooleanField(default=False, verbose_name='reading_books'),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='hobby2',
            field=models.BooleanField(default=False, verbose_name='travelling'),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='hobby3',
            field=models.BooleanField(default=False, verbose_name='listening_music'),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='hobby4',
            field=models.BooleanField(default=False, verbose_name='coding'),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='hobby5',
            field=models.BooleanField(default=False, verbose_name='sports'),
        ),
    ]