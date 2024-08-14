from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.documents.models import Document
from wagtail.fields import StreamField
from wagtail.models import Page

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock


# Landing-section
class LandingBlock(blocks.StructBlock):
    attention_title = blocks.CharBlock(
        verbose_name="attention_title",
        default='title',
        max_length=50,
        help_text="first attention for visitors"
    )

    catcher = blocks.CharBlock(
        verbose_name="catcher",
        default='write something great',
        max_length=200,
        help_text="catch your visitors"
    )

    background_image_landing = ImageChooserBlock(
        required=False,
        help_text="Background image for the landing page"
    )

    class Meta:
        template = 'home/sections/landing.html'
        icon = "view"
        label = "Landing section"

# ===================

# Introduction-section

class Introduction(blocks.StructBlock):
    greeting = blocks.CharBlock(required=False, max_length=50)
    introduction_text = blocks.TextBlock()
    personal_image = ImageChooserBlock()

    class Meta:
        template = 'home/sections/introduction.html'
        icon = "user"
        label = "Introduction section"  #


# ====================


# Project

class OrderedProjects(blocks.StructBlock):
    projects = blocks.StreamBlock([
        ('project', SnippetChooserBlock('streams.Project')),
    ], null=True, blank=True)

    class Meta:
        label = "OrderedProjects"
        icon = "list-ul"
        template = "home/sections/project/ordered_projects.html"


# =====================


# Motivation

class Motivation(blocks.StructBlock):
    quotes = blocks.StreamBlock([
        ('quote', SnippetChooserBlock('streams.Quote')),
    ])

    final_words = blocks.TextBlock(required=False,
                                   max_length=200)

    class Meta:
        label = "Motivation"
        icon = "openquote"
        template = "home/sections/motivation.html"


class HomePage(Page):
    cv = models.ForeignKey(
        Document,
        verbose_name="CV",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = StreamField([
        ('landing_section', LandingBlock()),
        ('introduction_section', Introduction()),
        ('project', OrderedProjects()),
        ('motivation', Motivation()),

    ], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('cv'),
        FieldPanel('body'),
    ]
