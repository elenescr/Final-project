# Generated by Django 5.0.6 on 2024-07-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/images/avatar.svg', null=True, upload_to=''),
        ),
    ]