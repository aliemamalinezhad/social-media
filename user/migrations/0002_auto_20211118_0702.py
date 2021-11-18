# Generated by Django 3.2.9 on 2021-11-18 07:02

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cover',
            field=models.ImageField(blank=True, max_length=128, null=True, upload_to=user.models.get_file_path, verbose_name='Cover'),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Email Verified'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Admin'),
        ),
        migrations.AddField(
            model_name='user',
            name='main_image',
            field=models.CharField(blank=True, max_length=1024, null=True, unique=True, verbose_name='Main Image'),
        ),
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False, verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=256, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Username'),
        ),
    ]
