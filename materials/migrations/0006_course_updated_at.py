# Generated by Django 5.0.7 on 2024-08-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0005_delete_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата последнего изменения"
            ),
        ),
    ]