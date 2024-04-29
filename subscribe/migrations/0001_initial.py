# Generated by Django 4.2.11 on 2024-04-29 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_id', to='user.user')),
                ('listener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listener_id', to='user.user')),
            ],
            options={
                'db_table': 'subscribe',
            },
        ),
    ]
