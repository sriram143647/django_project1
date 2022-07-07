# Generated by Django 4.0.4 on 2022-07-01 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customteam', '0001_initial'),
        ('customtask', '0002_customtask_team_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtask',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customteam.customteam'),
        ),
    ]