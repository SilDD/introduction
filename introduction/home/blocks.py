from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from streams.models import Skill





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
# =================================

# Skill

class SkillChoiceBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=False,
                              max_length=50)

    SKILL_TYPE_CHOICES = [
        ('hard', 'Hard Skill'),
        ('soft', 'Soft Skill'),
    ]

    skill_type = blocks.ChoiceBlock(
        choices=SKILL_TYPE_CHOICES,
        required=True,
        help_text="Choose whether to display Hard or Soft Skills"
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)

        # Filter the skills based on the selected skill_type
        selected_skill_type = value.get('skill_type')
        skills = Skill.objects.filter(skill_type=selected_skill_type)

        # Add the filtered skills to the context
        context['skills'] = skills
        return context

    class Meta:
        icon = "list-ul"
        label = "Skill Choice"
        template = "home/sections/devider.html"

# ========================