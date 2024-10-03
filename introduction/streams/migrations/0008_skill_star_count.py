# Generated by Django 5.0.8 on 2024-10-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0007_alter_quote_quote_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='star_count',
            field=models.IntegerField(blank=True, choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], help_text='Display the skill intensity for hard skills.', null=True),
        ),
    ]
