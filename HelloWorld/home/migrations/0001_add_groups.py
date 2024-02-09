# Generated by Django 5.0 on 2023-12-28 17:19

from django.db import migrations
from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission


def populate_groups(apps, schema_editor):
    """
    This function is run as an initial data migration at project initialization.
    Original migration created using:
        python manage.py makemigrations --empty LibraryApp
    On deploy use commands:
        python manage.py migrate LibraryApp 0001 --fake
        python manage.py migrate LibraryApp 0002
    """

    # Create user groups
    GROUPS = ['user', 'admin']
    user_group, ug_created = Group.objects.get_or_create(name=GROUPS[0])
    admin_group, ag_created = Group.objects.get_or_create(name=GROUPS[1])
    return


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(populate_groups),
    ]
