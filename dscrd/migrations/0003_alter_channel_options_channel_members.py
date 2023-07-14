# Generated by Django 4.2.1 on 2023-07-13 17:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dscrd', '0002_topic_channel_host_message_channel_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='channel',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
