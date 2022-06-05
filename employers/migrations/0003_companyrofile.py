# Generated by Django 4.0.4 on 2022-06-03 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employers', '0002_rename_job_comp_name_jobs_companyname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companyrofile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=100)),
                ('services', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
