from ariadne.contrib.federation import FederatedObjectType
from diagnosis_microservice.diagnosis.models import Diagnosis

diagnosis_federated_object = FederatedObjectType("Diagnosis")
patient_federated_object = FederatedObjectType("Patient")
doctor_federated_object = FederatedObjectType("Doctor")
print(">>>>>")
print(Diagnosis.objects.all())
@diagnosis_federated_object.reference_resolver
def get_diagnosis_by_uid(_,_info, representation):
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
    return {"license_number": obj["consulting_doctor"]["license_number"]}

@diagnosis_federated_object.field("visiting_patient")
def resolve_visiting_patient(obj, *_):
    return {"patient_number": obj["visiting_patient"]["patient_number"]}

@doctor_federated_object.field("diagnosis")
def resolve_doctor_diagnosis(obj, *_):
    return Diagnosis.objects.filter(consulting_doctor__license_number=obj["consulting_doctor"]["license_number"])

@patient_federated_object.field("diagnosis")
def resolve_patient_diagnosis(obj, *_):
    return Diagnosis.objects.filter(visiting_patient__patient_number=obj["visiting_patient"]["patient_number"])


#https://stackoverflow.com/questions/35133299/launch-a-shell-script-from-lambda-in-aws
#https://stackoverflow.com/questions/60566124/execute-python-script-on-ec2-instance-via-aws-lambda
#https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/
#https://github.com/skipdev/Python-Booking-System
#https://github.com/mdave/pyappointment
#https://www.freecodecamp.org/news/introducing-timeboard-a-python-business-calendar-package-a2335898c697/
#https://pypi.org/project/django-diary/
#https://github.com/saroarjahan/Django-appointment-and-booking-system
#https://forum.djangoproject.com/t/making-a-recurrent-appointment-scheduling-software-with-django-and-python/2547
#https://steelkiwi.com/projects/a-system-for-medical-appointment-scheduling/
#https://teamtreehouse.com/community/how-to-model-a-planning-appointment-for-doctors-in-django