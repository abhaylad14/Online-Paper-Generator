# Generated by Django 2.1.15 on 2020-04-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlinePaperGenerator', '0013_auto_20200425_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]
