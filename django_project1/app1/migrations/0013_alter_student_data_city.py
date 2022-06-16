# Generated by Django 4.0.4 on 2022-06-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_student_data_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='city',
            field=models.CharField(choices=[('S', 'Surat'), ('R', 'Rajkot'), ('A', 'Ahmedabad'), ('V', 'Vadodara')], default='S', max_length=1),
        ),
    ]
