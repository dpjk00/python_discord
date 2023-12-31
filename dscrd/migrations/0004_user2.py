# Generated by Django 4.2.1 on 2023-07-14 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dscrd', '0003_alter_channel_options_channel_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channels', models.ManyToManyField(blank=True, related_name='channels', to='dscrd.channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
