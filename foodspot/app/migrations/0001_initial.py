# Generated by Django 4.1 on 2022-11-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('state', models.TextField()),
                ('city', models.TextField()),
                ('address', models.TextField()),
                ('phnnumber', models.TextField()),
            ],
        ),
    ]