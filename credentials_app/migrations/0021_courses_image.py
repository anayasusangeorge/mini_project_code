# Generated by Django 4.1.1 on 2022-10-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials_app', '0020_courses_delete_course_remove_user_logins_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(default=0, upload_to='pics'),
        ),
    ]
