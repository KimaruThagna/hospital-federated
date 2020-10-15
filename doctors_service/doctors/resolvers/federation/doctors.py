from ariadne.contrib.federation import FederatedObjectType

from doctors_service.doctors.models import Doctor

doctor_federated_object = FederatedObjectType("Doctor")


@doctor_federated_object.reference_resolver
def get_doctor_by_uid(_, _info, representation):
    return Doctor.objects.get(license_number=representation.get("license_number"))


@doctor_federated_object.field("uid")
def resolve_id(obj, *_):
    return obj.uid


@doctor_federated_object.field("indexingId")
def resolve_indexing_id(obj, *_):
    return obj.indexing_id


@doctor_federated_object.field("first_name")
def resolve_first_name(obj, *_):
    return obj.first_name


@doctor_federated_object.field("last_name")
def resolve_last_name(obj, *_):
    return obj.last_name


@doctor_federated_object.field("specialization")
def resolve_specialization(obj, *_):
    return obj.specialization


@doctor_federated_object.field("license_number")
def resolve_license_number(obj, *_):
    return obj.license_number


@doctor_federated_object.field("county")
def resolve_county(obj, *_):
    return obj.county
