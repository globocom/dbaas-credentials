# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import factory
from dbaas_credentials import models
from physical.tests.factory import EnvironmentFactory


class CredentialTypeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.CredentialType

    name = factory.Sequence(lambda n: 'name_{0}'.format(n))
    type = 1

class CredentialFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Credential

    user = factory.Sequence(lambda n: 'name_{0}'.format(n))
    password = factory.Sequence(lambda n: 'pass_{0}'.format(n))
    integration_type = factory.SubFactory(CredentialTypeFactory)
    token = factory.Sequence(lambda n: 'token_{0}'.format(n))
    secret = factory.Sequence(lambda n: 'secret_{0}'.format(n))
    endpoint =factory.Sequence(lambda n: 'endpoint_{0}'.format(n))
    project = factory.Sequence(lambda n: 'project.glb_{0}'.format(n))
    team = factory.Sequence(lambda n: 'team.glb_{0}'.format(n))

    @factory.post_generation
    def environments(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for env in extracted:
                self.environments.add(env)
        else:
            self.environments.add(EnvironmentFactory())
