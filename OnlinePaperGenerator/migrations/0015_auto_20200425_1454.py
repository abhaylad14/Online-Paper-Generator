# Generated by Django 2.1.15 on 2020-04-25 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlinePaperGenerator', '0014_questionbank'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionbank',
            name='chapterno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionbank',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionbank',
            name='subject_code',
            field=models.IntegerField(default=0),
        ),
    ]
