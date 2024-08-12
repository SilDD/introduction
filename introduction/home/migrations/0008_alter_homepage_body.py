# Generated by Django 5.0.8 on 2024-08-12 21:22

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('landing_section', 3), ('introduction_section', 6), ('project', 7)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'default': 'title', 'help_text': 'first attention for visitors', 'max_length': 50, 'verbose_name': 'attention_title'}), 1: ('wagtail.blocks.CharBlock', (), {'default': 'write something great', 'help_text': 'catch your visitors', 'max_length': 200, 'verbose_name': 'catcher'}), 2: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Background image for the landing page', 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('attention_title', 0), ('catcher', 1), ('background_image_landing', 2)]], {}), 4: ('wagtail.blocks.TextBlock', (), {}), 5: ('wagtail.images.blocks.ImageChooserBlock', (), {}), 6: ('wagtail.blocks.StructBlock', [[('introduction_text', 4), ('personal_image', 5)]], {}), 7: ('wagtail.blocks.StreamBlock', [[]], {})}, null=True),
        ),
    ]
