# Generated by Django 2.0.6 on 2018-06-06 06:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(default=2, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
