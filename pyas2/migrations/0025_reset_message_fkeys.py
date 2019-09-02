# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0024_change_organization_partner_pkeys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='organization',
            field=models.ForeignKey(to='pyas2.Organization', null=True, db_constraint=True)
        ),
        migrations.AlterField(
            model_name='message',
            name='partner',
            field=models.ForeignKey(to='pyas2.Partner', null=True, db_constraint=True)
        )
    ]

