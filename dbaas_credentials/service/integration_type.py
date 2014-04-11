from django_services import service
from ..models import CredentialType


class CredentialTypeService(service.CRUDService):
    model_class = CredentialType