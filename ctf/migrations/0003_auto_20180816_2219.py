# Generated by Django 2.1 on 2018-08-16 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0002_auto_20180816_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.Topic'),
        ),
    ]
