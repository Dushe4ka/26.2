# Generated by Django 5.0.7 on 2024-07-25 10:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_subscription"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                (
                    "datetime_payment",
                    models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты"),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="сумма оплаты"
                    ),
                ),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("Наличные", "Cash"), ("Переводом", "Transfer")],
                        max_length=16,
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "session_id",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name=" id сессии"
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        max_length=400,
                        null=True,
                        verbose_name="Ссылка на оплату",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="payment",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="payment",
                        to="materials.course",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="payment",
                        to="materials.lesson",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата",
                "verbose_name_plural": "Оплаты",
            },
        ),
    ]