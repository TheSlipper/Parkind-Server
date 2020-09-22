# Generated by Django 3.1.1 on 2020-09-22 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateField()),
                ('icon_bg_type', models.CharField(default='success', max_length=30)),
                ('icon_type', models.CharField(default='file', max_length=30)),
                ('message', models.CharField(default='Notification message content', max_length=100)),
                ('redirect_url', models.CharField(default='#', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
