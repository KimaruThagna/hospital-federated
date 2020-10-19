import logging

from ariadne.contrib.federation import FederatedObjectType
from diagnosis.models import Diagnosis

patient_federated_type = FederatedObjectType("Patient")


class Patient:
    def __init__(self, uid):
        self.uid = uid


@patient_federated_type.reference_resolver
def get_patient_by_uid(_, _info, representation):
    try:
        uid = representation.get("uid")
        return Patient(uid)
    except Exception as error:
        logging.error(error)
        return None


@patient_federated_type.field("uid")
def resolve_uid(obj, *_):
    try:
        if isinstance(obj, dict):
            return obj.get("uid")
        if isinstance(obj, Patient):
            return obj.uid
    except Exception as error:
        logging.error(error)
        return None


@patient_federated_type.field("diagnosis")
def resolve_diagnosis(obj, *_):
    try:
        return Diagnosis.objects.filter(visiting_patient=obj.uid)
    except Exception as error:
        logging.error(error)
        return None
