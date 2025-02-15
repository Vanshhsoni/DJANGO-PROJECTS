# Generated by Django 5.1.1 on 2024-10-19 13:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feed", "0006_remove_post_created_at_alter_post_image_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="post_images/"),
        ),
    ]
