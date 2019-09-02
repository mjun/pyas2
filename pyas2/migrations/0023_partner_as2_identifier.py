# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models import F


def migrate_as2_identifiers_for_existing_partners(apps, schema_editor):
    Partner = apps.get_model("pyas2", "Partner")
    Partner.objects.all().update(as2_identifier=F('as2_name'))


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0022_partner_extra_headers'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='as2_identifier',
            field=models.CharField(default='as2_identifier', max_length=100, verbose_name='AS2 Identifier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Organization Name'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='as2_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='AS2 Name'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='extra_headers',
            field=models.TextField(blank=True, null=True, verbose_name='Extra Headers'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Partner Name'),
        ),
        migrations.RunPython(migrate_as2_identifiers_for_existing_partners),
    ]
