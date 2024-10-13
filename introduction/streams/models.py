from django.db import models
from wagtail import blocks

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from wagtail.snippets.models import register_snippet

@register_snippet
class Project(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField(max_length=500, blank=True, null=True)

    images = StreamField([
        ('image', ImageChooserBlock(label="Bild")),
    ], blank=True)

    links =  StreamField(
    [
        ('link', blocks.StructBlock([
            ('link_title', blocks.CharBlock(required=False, label="Link Title")),
            ('link_url', blocks.URLBlock(required=True, label="Link URL"))
        ]))
    ],
    null=True,
    blank=True
)
    skillset = StreamField([
        ('skill', SnippetChooserBlock('streams.Skill')),
    ], null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('images'),
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

    STARS = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    star_count = models.IntegerField(
        choices=STARS,
        blank=True,
        null=True,
        help_text="Display the skill intensity for hard skills."
    )

    skill_type = models.CharField(
        max_length=4,
        choices=SKILL_CHOICES,
        default='hard',
        help_text="Select whether this is a Hard Skill or Soft Skill")

    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
        FieldPanel('skill_type'),
        FieldPanel('star_count'),
    ]

    def __str__(self):
        return self.title




@register_snippet
class Quote(models.Model):
    quote_text = models.TextField(
        max_length=200,
        verbose_name="Quote",
        help_text="Enter the text of the quote here.",
    )

    author = models.CharField(
        max_length=255,
        verbose_name="Author",
        help_text="Name of the person who said or wrote the quote.",
        blank=True,
        null=True,
    )


    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name="Author's Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('quote_text'),
            FieldPanel('author'),
            FieldPanel('image'),

        ], heading="Quote Details")
    ]

    def __str__(self):
        return f"{self.quote_text[:50]}{'...' if len(self.quote_text) > 50 else ''} - {self.author or 'Unknown'}"

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"