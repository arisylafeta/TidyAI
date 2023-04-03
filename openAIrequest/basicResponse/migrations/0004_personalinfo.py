# Generated by Django 4.1 on 2023-04-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicResponse', '0003_rename_ai_answer_answer_aianswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('address_line', models.TextField()),
                ('email_addres', models.EmailField(max_length=254)),
                ('biography', models.TextField()),
            ],
        ),
    ]