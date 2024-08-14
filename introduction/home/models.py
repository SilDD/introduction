from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.documents.models import Document
from wagtail.fields import StreamField
from wagtail.models import Page

from home.blocks import LandingBlock, Introduction, OrderedProjects, Motivation, SkillChoiceBlock


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
        ('skill_set', SkillChoiceBlock()),

    ], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('cv'),
        FieldPanel('body'),
    ]
