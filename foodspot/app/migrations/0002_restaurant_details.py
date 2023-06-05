# Generated by Django 4.1 on 2022-11-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.TextField()),
                ('password', models.TextField()),
                ('state', models.TextField()),
                ('city', models.TextField()),
                ('address', models.TextField()),
                ('phnnumber', models.TextField()),
                ('email', models.TextField()),
                ('logo', models.ImageField(upload_to='images/')),
                ('about_restaurant', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]