# Generated by Django 5.0.3 on 2024-04-18 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ContactUs.contactus'),
        ),
    ]
