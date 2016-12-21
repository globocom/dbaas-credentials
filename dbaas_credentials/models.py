# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
import simple_audit
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields.encrypted import EncryptedCharField
from util.models import BaseModel
from physical.models import Environment

CACHE_MISS = object()

LOG = logging.getLogger(__name__)


class CredentialType(BaseModel):
    CLOUDSTACK = 1
    NFSAAS = 2
    DBMONITOR = 3
    ZABBIX = 4
    FLIPPER = 5
    VM = 6
    MYSQL = 7
    MONGODB = 8
    DNSAPI = 9
    ACLAPI = 10
    LAAS = 11
    LOGNIT = 12
    NETWORKAPI = 13
    GRAPHITE = 14
    STATSD = 15
    REDIS = 16
    DBAAS_SERVICES_ANALYZING = 17
    FOXHA = 18
    FOREMAN = 19
    MYSQL_REPLICA = 20
    MYSQL_FOXHA = 21
    FAAS = 22
    GRAFANA = 23

    INTEGRATION_CHOICES = (
        (CLOUDSTACK, 'Cloud Stack'),
        (NFSAAS, 'NFS as a Service'),
        (DBMONITOR, 'Database Monitor'),
        (ZABBIX, 'Zabbix'),
        (FLIPPER, 'Flipper'),
        (VM, 'Virtual machine credentials'),
        (MYSQL, 'MySQL credentials'),
        (MONGODB, 'MongoDB credentials'),
        (DNSAPI, 'DNS API'),
        (ACLAPI, 'ACL API'),
        (LAAS, 'Log as a Service'),
        (LOGNIT, 'Lognit'),
        (NETWORKAPI, 'Network API'),
        (GRAPHITE, 'Graphite'),
        (STATSD, 'Statsd'),
        (REDIS, 'Redis credentials'),
        (DBAAS_SERVICES_ANALYZING, 'DBaaSSAnalyzing'),
        (FOXHA, 'FoxHA'),
        (FOREMAN, 'Foreman'),
        (MYSQL_REPLICA, 'MySQL Replica'),
        (MYSQL_FOXHA, 'MySQL FoxHA'),
        (FAAS, 'FaaS'),
        (GRAFANA, 'Grafana'),
    )
    name = models.CharField(verbose_name=_("Name"),
                            max_length=100,
                            help_text="Integration Name")
    type = models.IntegerField(choices=INTEGRATION_CHOICES,
                               default=0)

    class Meta:
        permissions = (
            ("view_integrationtype", "Can view integration type."),
        )


class Credential(BaseModel):

    user = models.CharField(
        verbose_name=_("User"), max_length=100,
        help_text=_("User used to authenticate."), blank=True, null=True
    )
    password = EncryptedCharField(
        verbose_name=_("Password"), max_length=255, blank=True, null=True
    )
    integration_type = models.ForeignKey(
        CredentialType, related_name="integration_type",
        on_delete=models.PROTECT
    )
    token = models.CharField(
        verbose_name=_("Authentication Token"), max_length=255, blank=True,
        null=True
    )
    secret = EncryptedCharField(
        verbose_name=_("Secret"), max_length=255, blank=True, null=False
    )
    endpoint = models.CharField(
        verbose_name=_("Endpoint"), max_length=255,
        help_text=_(
            "Usually it is in the form host:port. Authentication endpoint."
        ), blank=False, null=False
    )
    environments = models.ManyToManyField(Environment)
    project = models.CharField(
        verbose_name=_("Project"), max_length=255, blank=True, null=True
    )
    team = models.CharField(
        verbose_name=_("Team"), max_length=255, blank=True, null=True,
        default=None
    )

    def __unicode__(self):
        return "%s" % (self.id)

    def environment(self):
        return ', '.join([e.name for e in self.environments.all()])

    class Meta:
        permissions = (
            ("view_integrationcredential", "Can view integration credential."),
        )

    def get_parameter_by_name(self, name):
        try:
            value = Parameter.objects.get(credential=self, name=name).value
            LOG.debug("Parameter '%s': '%s'", name, value)
            return value
        except Parameter.DoesNotExist:
            LOG.warning("Parameter %s not found" % name)
            return None
        except Exception as e:
            LOG.warning(
                "ops.. could not retrieve parameter value for %s: %s" % (name, e))
            return None

    def get_parameters_by_group(self, group_name):
        try:
            parameter_query = Parameter.objects.filter(
                credential=self, name__startswith=group_name
            ).values('name', 'value')

            if len(parameter_query) < 1:
                raise Exception('No parameters available')

            return {
                parameter['name'].split(group_name + '_')[1]: parameter['value']
                for parameter in parameter_query
            }
        except Exception as e:
            LOG.warning(
                "ops.. could not retrieve parameters values for  group %s: %s" % (group_name, e))
            return {}


class Parameter(BaseModel):

    name = models.CharField(verbose_name=_("Parameter name"), max_length=100)
    value = models.CharField(verbose_name=_("Parameter value"), max_length=255)
    description = models.CharField(
        verbose_name=_("Description"), max_length=255, null=True, blank=True
    )
    credential = models.ForeignKey(
        Credential, related_name="credential_parameters"
    )

    class Meta:
        unique_together = (
            ('credential', 'name'),
        )

simple_audit.register(Credential, CredentialType, Parameter)
