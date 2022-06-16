# Generated by Django 4.0.4 on 2022-06-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_student_data_hobby1_alter_student_data_hobby2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='city',
            field=models.CharField(choices=[('ST', 'Surat'), ('RJ', 'Rajkot'), ('AH', 'Ahmedabad'), ('VD', 'Vadodara')], default='ST', max_length=2),
        ),
    ]
