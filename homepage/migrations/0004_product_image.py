# Generated by Django 5.0 on 2024-01-01 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_orders_product_delete_member_orders_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='No Inage available', max_length=255),
        ),
    ]
