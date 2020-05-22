# Generated by Django 2.1.15 on 2020-04-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OnlinePaperGenerator', '0018_auto_20200429_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(default='', max_length=15)),
                ('chapterno', models.IntegerField(default=0)),
                ('marks', models.IntegerField(default=0)),
                ('difficulty', models.CharField(max_length=10)),
                ('priority', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(default='', max_length=15)),
                ('subject_name', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
                ('faculty', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
