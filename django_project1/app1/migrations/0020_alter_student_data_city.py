# Generated by Django 4.0.4 on 2022-06-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_alter_student_data_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='city',
            field=models.CharField(max_length=10),
        ),
    ]
