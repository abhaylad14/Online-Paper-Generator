# Generated by Django 2.1.15 on 2020-04-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlinePaperGenerator', '0002_auto_20200420_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='faculty',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
