# Generated by Django 4.1.7 on 2023-03-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Review", "0006_alter_faculty_semester"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faculty",
            name="semester",
            field=models.ManyToManyField(to="Review.semester"),
        ),
    ]
