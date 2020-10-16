from ariadne.contrib.federation import FederatedObjectType
from diagnosis.models import Diagnosis

diagnosis_federated_object = FederatedObjectType("Diagnosis")


@diagnosis_federated_object.reference_resolver
def get_diagnosis_by_uid(_, _info, representation):
    return Diagnosis.objects.get(uid=representation.get("uid"))


@diagnosis_federated_object.field("uid")
def resolve_id(obj, *_):
    return obj.uid


@diagnosis_federated_object.field("indexingId")
def resolve_indexing_id(obj, *_):
    return obj.indexing_id


@diagnosis_federated_object.field("diagnosis")
def resolve_diagnosis(obj, *_):
    return obj.diagnosis


@diagnosis_federated_object.field("consulting_doctor")
def resolve_consulting_doctor(obj, *_):
    return {"uid": obj.consulting_doctor}


@diagnosis_federated_object.field("visiting_patient")
def resolve_visiting_patient(obj, *_):
    return {"uid": obj.visiting_patient}
