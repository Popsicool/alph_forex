# Generated by Django 4.1 on 2022-09-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_payment_acc'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='account',
            field=models.PositiveIntegerField(default=123232),
            preserve_default=False,
        ),
    ]
