# Generated by Django 5.0.4 on 2024-04-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_rename_email_register_useremail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='shoes/')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
