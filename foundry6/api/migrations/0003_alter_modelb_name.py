# Generated by Django 4.2.4 on 2023-12-04 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_modelb_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelb",
            name="name",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nested",
                to="api.modela",
            ),
        ),
    ]
