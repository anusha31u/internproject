# Generated by Django 5.0.6 on 2024-05-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myanu', '0004_paragraph_user_createdat_user_dob_user_modifiedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
