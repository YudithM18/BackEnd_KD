# Generated by Django 5.1.2 on 2024-12-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendations_url', models.TextField()),
                ('tips_title', models.CharField(max_length=100)),
                ('tips_description', models.TextField()),
            ],
        ),
    ]