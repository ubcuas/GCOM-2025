# Generated by Django 5.0.6 on 2024-10-06 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nav", "0002_route_waypoint_route"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="waypoint",
            name="route",
        ),
        migrations.AddField(
            model_name="orderedwaypoint",
            name="route",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="waypoints",
                to="nav.route",
            ),
            preserve_default=False,
        ),
    ]
