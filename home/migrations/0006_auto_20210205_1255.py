# Generated by Django 3.1.5 on 2021-02-05 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_ourworks_workdone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workdone',
            name='our_works',
        ),
        migrations.DeleteModel(
            name='OurWorks',
        ),
        migrations.DeleteModel(
            name='WorkDone',
        ),
    ]
