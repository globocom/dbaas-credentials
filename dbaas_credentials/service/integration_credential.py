from django_services import service
from ..models import Credential


class IntegrationCredentialService(service.CRUDService):
    model_class = Credential
