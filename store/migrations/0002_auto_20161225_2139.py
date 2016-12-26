# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='latitude',
            field=models.FloatField(default=48.7533348, max_length=20),
        ),
        migrations.AddField(
            model_name='review',
            name='longitude',
            field=models.FloatField(default=21.8819297, max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='books/empty_cover.jpg', upload_to=store.models.cover_upload_path),
        ),
    ]
