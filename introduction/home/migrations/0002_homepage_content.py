# Generated by Django 4.2.2 on 2024-08-04 21:10

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('landing', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50, required=True)), ('catcher', wagtail.blocks.CharBlock(max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('cv', wagtail.documents.blocks.DocumentChooserBlock(required=False))]))], blank=True, null=True, use_json_field=True),
        ),
    ]