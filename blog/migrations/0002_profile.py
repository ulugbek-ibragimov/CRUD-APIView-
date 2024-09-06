# Generated by Django 5.1 on 2024-09-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True, verbose_name='User name')),
                ('lastname', models.CharField(blank=True, max_length=100, null=True, verbose_name='User lastname')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
    ]
