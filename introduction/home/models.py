from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.documents.models import Document
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page
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
    introduction_text = blocks.TextBlock()
    personal_image = ImageChooserBlock()

    class Meta:
        template = 'home/sections/introduction.html'
        icon = "user"
        label = "Introduction section"#

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

    ], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('cv'),
        FieldPanel('body'),
    ]
