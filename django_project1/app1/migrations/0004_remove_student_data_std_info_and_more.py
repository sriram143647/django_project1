# Generated by Django 4.0.4 on 2022-05-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_student_data_std_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_data',
            name='std_info',
        ),
        migrations.AlterField(
            model_name='student_data',
            name='std_phone',
            field=models.CharField(max_length=10),
        ),
    ]
