# Generated by Django 4.1.1 on 2022-10-13 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interapp', '0006_duaration_alter_course_detail_course_week'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='duaration',
            new_name='duration',
        ),
    ]
