from django.db import models
from wagtail.admin import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.documents.models import Document
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page


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
        icon = "view"
        label = "Landing section"


class Introduction(blocks.StructBlock):
    introduction_text = blocks.RichTextBlock()
    personal_image = ImageChooserBlock()

    class Meta:
        icon = "user"
        label = "Introduction section"


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
        ('introduction_section', Introduction())

    ], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('cv'),
        FieldPanel('body'),
    ]
