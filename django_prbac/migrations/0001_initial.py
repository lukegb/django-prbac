# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_prbac.fields
from django.conf import settings
import json_field.fields
import django_prbac.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment', json_field.fields.JSONField(default={}, help_text='Assignment from parameters (strings) to values (any JSON-compatible value)', blank=True)),
            ],
            options={
            },
            bases=(django_prbac.models.ValidatingModel, models.Model),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(help_text='The formal slug for this role, which should be unique', unique=True, max_length=256)),
                ('name', models.CharField(help_text='The friendly name for this role to present to users; this need not be unique.', max_length=256)),
                ('description', models.TextField(default='', help_text='A long-form description of the intended semantics of this role.', blank=True)),
                ('parameters', django_prbac.fields.StringSetField(default=[], help_text='A set of strings which are the parameters for this role. Entered as a JSON list.', blank=True)),
            ],
            options={
            },
            bases=(django_prbac.models.ValidatingModel, models.Model),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.OneToOneField(related_name='user_role', to='django_prbac.Role')),
                ('user', models.OneToOneField(related_name='prbac_role', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(django_prbac.models.ValidatingModel, models.Model),
        ),
        migrations.AddField(
            model_name='grant',
            name='from_role',
            field=models.ForeignKey(related_name='memberships_granted', to='django_prbac.Role', help_text='The sub-role begin granted membership or permission'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grant',
            name='to_role',
            field=models.ForeignKey(related_name='members', to='django_prbac.Role', help_text='The super-role or permission being given'),
            preserve_default=True,
        ),
    ]
