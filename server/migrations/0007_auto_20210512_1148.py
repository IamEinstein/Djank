# Generated by Django 3.1.8 on 2021-05-12 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_user_email_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discord_account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.user'),
        ),
    ]
