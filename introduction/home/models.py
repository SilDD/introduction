from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.documents.models import Document

from wagtail.models import Page


class HomePage(Page):
    landing_title = models.CharField(verbose_name="attention_title",
                                     default='title',
                                     max_length=50,
                                     null=False,
                                     help_text="first attention for visitors"
                                     )

    catcher = models.CharField(verbose_name="catcher",
                               default='write something greate',
                               max_length=200,
                               null=False,
                               help_text="catch your visitors"
                               )

    landing_image = models.ForeignKey('wagtailimages.Image',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      related_name='+',
                                      verbose_name="background_image_landing")

    cv = models.ForeignKey(
        Document,
        verbose_name="CV",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('landing_title'),
        FieldPanel('catcher'),
        FieldPanel('landing_image'),
        FieldPanel('cv')
    ]
