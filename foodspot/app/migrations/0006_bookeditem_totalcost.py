# Generated by Django 4.2 on 2023-05-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_bookeditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookeditem',
            name='totalcost',
            field=models.TextField(blank=True),
        ),
    ]
