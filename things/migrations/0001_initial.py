# Generated by Django 4.2.6 on 2023-10-10 21:33

from django.db import migrations, models
import things.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(blank=True, max_length=120)),
                ('quantity', models.IntegerField(validators=[things.models.validate_quantity])),
            ],
        ),
    ]
