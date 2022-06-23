# Generated by Django 4.0.4 on 2022-06-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_alter_student_data_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='city',
            field=models.CharField(choices=[('ST', 'Surat'), ('RJ', 'Rajkot'), ('AH', 'Ahmedabad'), ('VD', 'Vadodara')], default='S', max_length=10),
        ),
    ]