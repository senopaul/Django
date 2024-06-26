# Generated by Django 5.0.3 on 2024-04-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=50)),
                ('email', models.EmailField(default='0', max_length=50)),
                ('phone', models.CharField(default='0', max_length=10)),
                ('content', models.TextField(default='0', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
