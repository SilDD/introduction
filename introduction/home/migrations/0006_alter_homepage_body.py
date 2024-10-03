# Generated by Django 5.0.8 on 2024-10-03 18:41

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('landing_section', 6), ('introduction_section', 10), ('project', 13), ('motivation', 17), ('skill_set', 20)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'default': 'title', 'help_text': 'first attention for visitors', 'max_length': 50, 'required': False, 'verbose_name': 'attention_title'}), 1: ('wagtail.blocks.CharBlock', (), {'default': 'title', 'help_text': 'is shown in Navigation', 'max_length': 50, 'required': False, 'verbose_name': 'menu title'}), 2: ('wagtail.blocks.BooleanBlock', (), {'required': False}), 3: ('wagtail.blocks.TextBlock', (), {'default': 'Description', 'help_text': 'Optional description if needed', 'required': False, 'verbose_name': 'Block description'}), 4: ('wagtail.blocks.CharBlock', (), {'default': 'write something great', 'help_text': 'catch your visitors', 'max_length': 200, 'verbose_name': 'catcher'}), 5: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Background image for the landing page', 'required': False}), 6: ('wagtail.blocks.StructBlock', [[('attention_title', 0), ('menu_title', 1), ('in_menu', 2), ('description', 3), ('catcher', 4), ('background_image_landing', 5)]], {}), 7: ('wagtail.blocks.CharBlock', (), {'max_length': 50, 'required': False}), 8: ('wagtail.blocks.TextBlock', (), {}), 9: ('wagtail.images.blocks.ImageChooserBlock', (), {}), 10: ('wagtail.blocks.StructBlock', [[('attention_title', 0), ('menu_title', 1), ('in_menu', 2), ('description', 3), ('greeting', 7), ('introduction_text', 8), ('personal_image', 9)]], {}), 11: ('wagtail.snippets.blocks.SnippetChooserBlock', ('streams.Project',), {}), 12: ('wagtail.blocks.StreamBlock', [[('project', 11)]], {'blank': True, 'null': True}), 13: ('wagtail.blocks.StructBlock', [[('attention_title', 0), ('menu_title', 1), ('in_menu', 2), ('description', 3), ('projects', 12)]], {}), 14: ('wagtail.snippets.blocks.SnippetChooserBlock', ('streams.Quote',), {}), 15: ('wagtail.blocks.StreamBlock', [[('quote', 14)]], {}), 16: ('wagtail.blocks.TextBlock', (), {'max_length': 200, 'required': False}), 17: ('wagtail.blocks.StructBlock', [[('attention_title', 0), ('menu_title', 1), ('in_menu', 2), ('description', 3), ('quotes', 15), ('final_words', 16)]], {}), 18: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('hard', 'Hard Skill'), ('soft', 'Soft Skill')], 'help_text': 'Choose whether to display Hard or Soft Skills'}), 19: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], 'help_text': 'Display the skill intensity for hard skills.', 'required': False}), 20: ('wagtail.blocks.StructBlock', [[('attention_title', 0), ('menu_title', 1), ('in_menu', 2), ('description', 3), ('skill_type', 18), ('star_count', 19)]], {})}, null=True),
        ),
    ]
