# Generated by Django 2.1 on 2018-08-16 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='赛事名称')),
                ('description', models.TextField(blank=True, default='', verbose_name='赛事描述')),
                ('start_time', models.DateTimeField(verbose_name='开赛时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solve_time', models.DateTimeField(verbose_name='解题时间')),
                ('score', models.IntegerField(default=0, verbose_name='题目分值')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='赛题名称')),
                ('address', models.CharField(blank=True, default='', max_length=50, verbose_name='比赛地址')),
                ('description', models.TextField(blank=True, default='', verbose_name='题目描述')),
                ('score', models.IntegerField(default=0, verbose_name='分值')),
                ('solve_num', models.IntegerField(default=0, verbose_name='解题人数')),
                ('flag', models.CharField(blank=True, default='', max_length=64, verbose_name='flag')),
                ('in_progress', models.BooleanField(default=False, verbose_name='是否正在进行')),
                ('release_time', models.DateTimeField(verbose_name='放出时间')),
                ('topic_type', models.CharField(blank=True, choices=[('Web', 'Web'), ('Pwn', 'Pwn'), ('Reverse', 'Reverse'), ('Crypto', 'Crpyto'), ('Mobile', 'Mobile'), ('Misc', 'Misc')], max_length=10, verbose_name='题目类型')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.Competition')),
            ],
        ),
    ]