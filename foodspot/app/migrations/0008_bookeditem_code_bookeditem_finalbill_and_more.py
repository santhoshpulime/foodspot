# Generated by Django 4.2 on 2023-05-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_order_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookeditem',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bookeditem',
            name='finalbill',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order_history',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order_history',
            name='finalbill',
            field=models.TextField(blank=True),
        ),
    ]
