# Generated by Django 3.2 on 2021-05-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210503_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='enrollment',
            field=models.BooleanField(default=False),
        ),
    ]
