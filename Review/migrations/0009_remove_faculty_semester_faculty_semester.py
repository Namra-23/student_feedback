# Generated by Django 4.1.7 on 2023-03-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Review", "0008_remove_faculty_semester_faculty_semester"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="faculty",
            name="semester",
        ),
        migrations.AddField(
            model_name="faculty",
            name="semester",
            field=models.ManyToManyField(to="Review.semester"),
        ),
    ]
