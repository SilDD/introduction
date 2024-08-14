# Generated by Django 5.0.8 on 2024-08-14 22:04

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('landing_section', 3), ('introduction_section', 7), ('project', 10), ('motivation', 14), ('skill_set', 16)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'default': 'title', 'help_text': 'first attention for visitors', 'max_length': 50, 'verbose_name': 'attention_title'}), 1: ('wagtail.blocks.CharBlock', (), {'default': 'write something great', 'help_text': 'catch your visitors', 'max_length': 200, 'verbose_name': 'catcher'}), 2: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Background image for the landing page', 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('attention_title', 0), ('catcher', 1), ('background_image_landing', 2)]], {}), 4: ('wagtail.blocks.CharBlock', (), {'max_length': 50, 'required': False}), 5: ('wagtail.blocks.TextBlock', (), {}), 6: ('wagtail.images.blocks.ImageChooserBlock', (), {}), 7: ('wagtail.blocks.StructBlock', [[('greeting', 4), ('introduction_text', 5), ('personal_image', 6)]], {}), 8: ('wagtail.snippets.blocks.SnippetChooserBlock', ('streams.Project',), {}), 9: ('wagtail.blocks.StreamBlock', [[('project', 8)]], {'blank': True, 'null': True}), 10: ('wagtail.blocks.StructBlock', [[('projects', 9)]], {}), 11: ('wagtail.snippets.blocks.SnippetChooserBlock', ('streams.Quote',), {}), 12: ('wagtail.blocks.StreamBlock', [[('quote', 11)]], {}), 13: ('wagtail.blocks.TextBlock', (), {'max_length': 200, 'required': False}), 14: ('wagtail.blocks.StructBlock', [[('quotes', 12), ('final_words', 13)]], {}), 15: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('hard', 'Hard Skills'), ('soft', 'Soft Skills')], 'help_text': 'Choose whether to display all Hard Skills or all Soft Skills'}), 16: ('wagtail.blocks.StructBlock', [[('header', 4), ('skill_type', 15)]], {})}, null=True),
        ),
    ]
