# Generated by Django 5.1.4 on 2025-01-05 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0003_alter_shippingaddress_shipping_address2_order_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="shipped",
            field=models.BooleanField(default=False),
        ),
    ]