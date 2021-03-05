# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from ..models import Parameter


class ParameterAdmin(admin.TabularInline):
    model = Parameter
    fields = ('name', 'value', 'description')
    extra = 1


class CredentialAdmin(admin.ModelAdmin):
    ordering = ['integration_type__name']
    search_fields = ("endpoint",)
    list_filter = ("integration_type", )
    list_display = ("integration_type", "environment", "endpoint", "user", )
    filter_horizontal = ("environments",)
    save_on_top = True

    inlines = [
        ParameterAdmin,
    ]
