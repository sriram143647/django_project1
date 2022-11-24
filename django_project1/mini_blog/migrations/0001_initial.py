# Generated by Django 4.0.4 on 2022-11-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0023_proxy_student_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('publish_date', models.DateField(null=True)),
                ('author', models.ManyToManyField(to='app1.student_data')),
            ],
        ),
    ]
