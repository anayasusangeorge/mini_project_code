# Generated by Django 4.1.1 on 2022-09-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials_app', '0012_alter_user_reg_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
