import models
import logging

LOG = logging.getLogger(__name__)


class Credential(object):

    @classmethod
    def get_credentials(cls, environment, integration):
        return models.Credential.objects.filter(
            environments=environment, integration_type=integration)[0]
