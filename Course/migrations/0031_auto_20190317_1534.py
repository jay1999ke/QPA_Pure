# Generated by Django 2.1.5 on 2019-03-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0030_auto_20190314_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='questions',
            field=models.ManyToManyField(related_name='question_of_course', to='Course.question'),
        ),
    ]