from django.db import models
from wagtail import blocks

from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock

from wagtail.snippets.models import register_snippet

@register_snippet
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    links = StreamField([
        ('link', blocks.URLBlock(required=True)),
    ], null=True, blank=True)

    skillset = StreamField([
        ('skill', SnippetChooserBlock('streams.Skill')),
    ], null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('links'),
        FieldPanel('skillset'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


@register_snippet
class Skill(models.Model):
    title = models.CharField(
        default="Bezeichnung",
        null=True,
        blank=False,
        max_length=50,
        verbose_name="Bezeichnung",
    )

    image = models.ForeignKey('wagtailimages.Image',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL,
                              related_name='+',
                              verbose_name="Logo")

    SKILL_CHOICES = [
        ('hard', 'Hard Skill'),
        ('soft', 'Soft Skill'),
    ]

    skill_type = models.CharField(
        max_length=4,
        choices=SKILL_CHOICES,
        default='hard',
        help_text="Select whether this is a Hard Skill or Soft Skill")

    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
        FieldPanel('skill_type'),
    ]

    def __str__(self):
        return self.title


