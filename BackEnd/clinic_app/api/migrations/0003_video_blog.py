# Generated by Django 5.1.2 on 2024-12-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_recommendations'),
    ]

    operations = [
        migrations.CreateModel(
            name='video_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_url', models.TextField()),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]