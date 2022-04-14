# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2022-03-22 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0023_partner_as2_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='status',
            field=models.CharField(choices=[('S', 'Success'), ('E', 'Error'), ('W', 'Warning')], max_length=2),
        ),
        migrations.AlterField(
            model_name='mdn',
            name='status',
            field=models.CharField(choices=[('S', 'Sent'), ('R', 'Received'), ('P', 'Pending')], max_length=2),
        ),
        migrations.AlterField(
            model_name='message',
            name='direction',
            field=models.CharField(choices=[('IN', 'Inbound'), ('OUT', 'Outbound')], max_length=5),
        ),
        migrations.AlterField(
            model_name='message',
            name='mdn_mode',
            field=models.CharField(choices=[('SYNC', 'Synchronous'), ('ASYNC', 'Asynchronous')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('S', 'Success'), ('E', 'Error'), ('W', 'Warning'), ('P', 'Pending'), ('R', 'Retry'), ('IP', 'In Process')], max_length=2),
        ),
        migrations.AlterField(
            model_name='partner',
            name='compress',
            field=models.BooleanField(default=True, verbose_name='Compress Message'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='content_type',
            field=models.CharField(choices=[('application/EDI-X12', 'application/EDI-X12'), ('application/EDIFACT', 'application/EDIFACT'), ('application/edi-consent', 'application/edi-consent'), ('application/XML', 'application/XML'), ('text/CSV', 'text/CSV')], default='application/edi-consent', max_length=100),
        ),
        migrations.AlterField(
            model_name='partner',
            name='encryption',
            field=models.CharField(blank=True, choices=[('des_ede3_cbc', '3DES'), ('des_cbc', 'DES'), ('aes_128_cbc', 'AES-128'), ('aes_192_cbc', 'AES-192'), ('aes_256_cbc', 'AES-256'), ('rc2_40_cbc', 'RC2-40')], max_length=20, null=True, verbose_name='Encrypt Message'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='http_auth',
            field=models.BooleanField(default=False, verbose_name='Enable Authentication'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='keep_filename',
            field=models.BooleanField(default=False, help_text='Use Original Filename to to store file on receipt, use this option only if you are sure partner sends unique names', verbose_name='Keep Original Filename'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='mdn_mode',
            field=models.CharField(blank=True, choices=[('SYNC', 'Synchronous'), ('ASYNC', 'Asynchronous')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='mdn_sign',
            field=models.CharField(blank=True, choices=[('sha1', 'SHA-1'), ('sha256', 'SHA-256')], max_length=20, null=True, verbose_name='Request Signed MDN'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='signature',
            field=models.CharField(blank=True, choices=[('sha1', 'SHA-1'), ('sha256', 'SHA-256')], max_length=20, null=True, verbose_name='Sign Message'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='subject',
            field=models.CharField(default='EDI Message sent using pyas2', max_length=255),
        ),
    ]
