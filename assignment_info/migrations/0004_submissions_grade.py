# Generated by Django 4.0.6 on 2023-04-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_info', '0003_auto_20201126_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]