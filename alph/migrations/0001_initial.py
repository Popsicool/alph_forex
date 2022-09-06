# Generated by Django 4.1 on 2022-09-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('existing', models.CharField(max_length=5)),
                ('phone_num', models.CharField(max_length=20, null=True)),
                ('account_number', models.CharField(max_length=20, null=True)),
                ('enquiry_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attended_to', models.BooleanField(default=False)),
            ],
        ),
    ]