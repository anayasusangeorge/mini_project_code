# Generated by Django 4.1.1 on 2022-10-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='video')),
                ('desc', models.TextField()),
                ('course_week', models.CharField(max_length=20)),
                ('price', models.CharField(default=0, max_length=10)),
                ('mentor', models.CharField(max_length=60)),
                ('outcomes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user_courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user_logins',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='None', max_length=20)),
                ('dob', models.DateField()),
                ('phonenumber', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]