# Generated by Django 4.2.1 on 2023-05-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinemas", "0003_rename_tickets_ticket_rename_move_showtime_movie_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="showtime",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
