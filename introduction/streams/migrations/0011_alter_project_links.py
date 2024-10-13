# Generated by Django 5.0.8 on 2024-10-13 18:55

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0010_alter_project_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='links',
            field=wagtail.fields.StreamField([('link', 2)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'label': 'Link Title', 'required': False}), 1: ('wagtail.blocks.URLBlock', (), {'label': 'Link URL', 'required': True}), 2: ('wagtail.blocks.StructBlock', [[('link_title', 0), ('link_url', 1)]], {})}, null=True),
        ),
    ]
