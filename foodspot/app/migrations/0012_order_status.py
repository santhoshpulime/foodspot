# Generated by Django 4.2 on 2023-05-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_bookeditem_confirmorder_by_restaurant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmorder_by_restaurant', models.TextField(blank=True)),
                ('item_not_yet', models.TextField(blank=True)),
                ('order_rejected', models.TextField(blank=True)),
            ],
        ),
    ]