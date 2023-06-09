# Generated by Django 4.2 on 2023-05-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_restaurants_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookeditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('user_id', models.TextField(blank=True)),
                ('item_id', models.TextField(blank=True)),
                ('item_name', models.TextField(blank=True)),
                ('item_cost', models.TextField(blank=True)),
                ('itemcategory', models.TextField(blank=True)),
                ('aboutitem', models.TextField(blank=True)),
                ('DateTimeField', models.DateTimeField(auto_now_add=True)),
                ('something', models.TextField(blank=True)),
            ],
        ),
    ]
