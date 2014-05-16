# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin


class CredentialAdmin(admin.ModelAdmin):
    search_fields = ("endpoint",)
    list_display = ("integration_type", "endpoint", "user",)
    filter_horizontal = ("environments",)
    save_on_top = True