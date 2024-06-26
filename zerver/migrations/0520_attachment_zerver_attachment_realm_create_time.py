# Generated by Django 5.0.6 on 2024-05-08 01:16

from django.contrib.postgres.operations import AddIndexConcurrently
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("zerver", "0519_archivetransaction_restored_timestamp"),
    ]

    operations = [
        AddIndexConcurrently(
            model_name="attachment",
            index=models.Index(
                models.F("realm"),
                models.F("create_time"),
                name="zerver_attachment_realm_create_time",
            ),
        ),
    ]
