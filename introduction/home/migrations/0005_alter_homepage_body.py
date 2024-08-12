# Generated by Django 4.2.2 on 2024-08-05 10:11

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_homepage_catcher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('landing_section', wagtail.blocks.StructBlock([('attention_title', wagtail.blocks.CharBlock(default='title', help_text='first attention for visitors', max_length=50, verbose_name='attention_title')), ('catcher', wagtail.blocks.CharBlock(default='write something great', help_text='catch your visitors', max_length=200, verbose_name='catcher')), ('background_image_landing', wagtail.images.blocks.ImageChooserBlock(help_text='Background image for the landing page', required=False))])), ('introduction_section', wagtail.blocks.StructBlock([('introduction_text', wagtail.blocks.TextBlock()), ('personal_image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True, use_json_field=True),
        ),
    ]