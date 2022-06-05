# Generated by Django 4.0.4 on 2022-06-03 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employers', '0003_companyrofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(null=True, upload_to='companyprofile')),
                ('services', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Companyrofile',
        ),
    ]