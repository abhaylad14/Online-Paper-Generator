# Generated by Django 2.1.15 on 2020-04-21 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlinePaperGenerator', '0009_remove_subject_sem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='subject',
        ),
    ]