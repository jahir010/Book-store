# Generated by Django 5.1.4 on 2024-12-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="old_cart",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
