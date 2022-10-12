# Generated by Django 4.1.2 on 2022-10-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ["model"]},
        ),
        migrations.AlterModelOptions(
            name="driver",
            options={
                "ordering": ["username"],
                "verbose_name": "Driver",
                "verbose_name_plural": "Drivers",
            },
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ["name"]},
        ),
        migrations.AddConstraint(
            model_name="manufacturer",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique_manufacturer_name"
            ),
        ),
    ]