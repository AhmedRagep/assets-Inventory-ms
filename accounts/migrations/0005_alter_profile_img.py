# Generated by Django 5.0.3 on 2024-04-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, upload_to='profile-image/'),
        ),
    ]
