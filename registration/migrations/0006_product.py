# Generated by Django 5.0.4 on 2024-04-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_rename_register_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
