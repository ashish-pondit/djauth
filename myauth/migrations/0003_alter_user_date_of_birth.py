# Generated by Django 4.2.1 on 2023-05-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myauth", "0002_alter_user_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]
