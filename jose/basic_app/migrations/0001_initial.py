# Generated by Django 5.0 on 2024-03-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=100)),
                ('contact_subject', models.CharField(max_length=100)),
                ('contact_message', models.CharField(max_length=900)),
            ],
        ),
    ]
