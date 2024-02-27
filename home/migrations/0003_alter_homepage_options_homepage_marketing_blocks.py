# Generated by Django 5.0.2 on 2024-02-27 17:47

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="homepage",
            options={"verbose_name": "Home Page"},
        ),
        migrations.AddField(
            model_name="homepage",
            name="marketing_blocks",
            field=wagtail.fields.StreamField(
                [
                    (
                        "marketing_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Enter the block title",
                                        required=False,
                                    ),
                                ),
                                (
                                    "content",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="Enter the block content",
                                        required=False,
                                    ),
                                ),
                                (
                                    "images",
                                    wagtail.blocks.ListBlock(
                                        wagtail.images.blocks.ImageChooserBlock(
                                            required=False
                                        ),
                                        help_text="Select one or two images for column display. Select three or more images for carousel display.",
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Select one image for background display.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "block_class",
                                    wagtail.blocks.CharBlock(
                                        default="vh-100 bg-secondary",
                                        form_classname="full title",
                                        help_text="Enter a CSS class for styling the marketing block",
                                        required=False,
                                    ),
                                ),
                                (
                                    "image_class",
                                    wagtail.blocks.CharBlock(
                                        default="img-thumbnail p-5",
                                        form_classname="full title",
                                        help_text="Enter a CSS class for styling the column display image(s)",
                                        required=False,
                                    ),
                                ),
                                (
                                    "layout_class",
                                    wagtail.blocks.CharBlock(
                                        default="d-flex flex-row",
                                        form_classname="full title",
                                        help_text="Enter a CSS class for styling the layout.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
