# Generated by Django 4.0.1 on 2022-05-17 05:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RcptGenerator', '0012_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
