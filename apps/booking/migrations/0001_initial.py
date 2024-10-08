# Generated by Django 4.2.15 on 2024-09-14 08:51

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("services", "0002_service_photo"),
        ("users", "0001_initial"),
        ("stylists", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("date_time", models.DateTimeField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Confirmed", "Confirmed"),
                            ("Cancelled", "Cancelled"),
                            ("Completed", "Completed"),
                            ("Updated", "Updated"),
                        ],
                        default="Confirmed",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "discount_percentage",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("code", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.IntegerField()),
                ("message", models.TextField()),
                (
                    "photo",
                    cloudinary.models.CloudinaryField(
                        default="placeholder", max_length=255, verbose_name="image"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "booking",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="booking.booking",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="booking",
            name="offer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="booking.offer",
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="services.service"
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="stylish",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="stylists.stylist"
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="user_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.userprofile"
            ),
        ),
    ]
