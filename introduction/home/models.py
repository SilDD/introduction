from tabnanny import verbose

from django.db import models

from wagtail.documents.models import Document
from wagtail.fields import StreamField
from wagtail.models import Page

from home.blocks import LandingBlock, Introduction, OrderedProjects, Motivation, SkillChoiceBlock

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel

)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)


@register_setting
class NavigationSettings(BaseGenericSetting):
    first_name = models.CharField(verbose_name="First name", blank=True, max_length=20)
    last_name = models.CharField(verbose_name="Last name", blank=True, max_length=20)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    email = models.EmailField(verbose_name="E-Mail_Adress", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('first_name'),
                FieldPanel('last_name'),
                FieldPanel("linkedin_url"),
                FieldPanel("github_url"),
                FieldPanel("email"),
            ],
            "Social settings",
        )
    ]


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
