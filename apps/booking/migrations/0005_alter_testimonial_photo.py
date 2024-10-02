# Generated by Django 4.2.15 on 2024-10-02 08:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0004_alter_testimonial_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="photo",
            field=cloudinary.models.CloudinaryField(
                blank=True,
                default="https://res.cloudinary.com/dx21s72fa/image/upload/v1727857392/w0wngka886ke3rcyr5gd.png",
                max_length=255,
                null=True,
                verbose_name="image",
            ),
        ),
    ]
