# Generated by Django 5.0.4 on 2024-05-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_subscribe_created_at_subscribe_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
