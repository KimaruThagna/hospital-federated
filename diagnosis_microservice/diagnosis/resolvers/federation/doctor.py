import logging

from ariadne.contrib.federation import FederatedObjectType
from diagnosis_microservice.diagnosis.models import Diagnosis

doctor_federated_type = FederatedObjectType("Doctor")


class Doctor:
    def __init__(self, uid):
        self.uid = uid


@doctor_federated_type.reference_resolver
def get_doctor_by_uid(_, _info, representation):
    try:
        uid = representation.get("uid")
        return Doctor(uid)
    except Exception as error:
        logging.error(error)
        return None


@doctor_federated_type.field("uid")
def resolve_uid(obj, *_):
    try:
        if isinstance(obj, dict):
            return obj.get("uid")
        if isinstance(obj, Doctor):
            return obj.uid
    except Exception as error:
        logging.error(error)
        return None


@doctor_federated_type.field("diagnosis")
def resolve_diagnosis(obj, *_):
    try:
        return Diagnosis.objects.filter(consulting_doctor=obj.uid)
    except Exception as error:
        logging.error(error)
        return None
