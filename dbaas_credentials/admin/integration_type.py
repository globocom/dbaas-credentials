# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin


class CredentialTypeAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ("name",)
    list_display = ("name", "type",)
    save_on_top = True
