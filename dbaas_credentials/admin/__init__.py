# -*- coding:utf-8 -*-
from django.contrib import admin
from .integration_credential import CredentialAdmin
from .integration_type import CredentialTypeAdmin
from .. import models

admin.site.register(models.CredentialType, CredentialTypeAdmin)
admin.site.register(models.Credential, CredentialAdmin)
