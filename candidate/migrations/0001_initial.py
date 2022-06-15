# Generated by Django 4.0.4 on 2022-06-15 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(choices=[('plustwo', '12th'), ('BSc', 'BSc'), ('BCA', 'BCA'), ('BCom', 'BCom'), ('MCA', 'MCA'), ('BTech', 'Btech'), ('Mtech', 'Mtect')], max_length=120)),
                ('skills', models.CharField(max_length=150)),
                ('dateofbirth', models.DateField(null=True)),
                ('place', models.CharField(max_length=65)),
                ('profile_pic', models.ImageField(upload_to='cand-profile')),
                ('experience', models.PositiveIntegerField(default=0)),
                ('resume', models.FileField(null=True, upload_to='cand-resume')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]