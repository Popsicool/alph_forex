# Generated by Django 4.1 on 2022-08-31 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authz', '0002_user_account_number_user_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account_number',
        ),
    ]