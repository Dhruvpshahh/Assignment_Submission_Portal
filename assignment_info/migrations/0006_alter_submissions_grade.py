# Generated by Django 4.0.6 on 2023-04-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_info', '0005_alter_submissions_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='grade',
            field=models.IntegerField(default=-1),
        ),
    ]