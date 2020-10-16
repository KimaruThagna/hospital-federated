from os.path import dirname, join

from ariadne import MutationType, QueryType, gql, load_schema_from_path
from ariadne.contrib.federation import make_federated_schema
from diagnosis.resolvers.federation.diagnosis import diagnosis_federated_object
from diagnosis.resolvers.federation.doctor import doctor_federated_type
from diagnosis.resolvers.federation.patient import patient_federated_type
from diagnosis.resolvers.mutations.diagnosis import *
from diagnosis.resolvers.queries.diagnosis import *


def load_typedef_from_schema():
    type_def = load_schema_from_path(join(dirname(dirname(__file__)), "./gql"))
    type_defs = gql(type_def)
    return type_defs


# query type and its fields resolvers
def bind_query_type_to_resolvers():
    query = QueryType()
    query.set_field("diagnosis_note", DiagnosisQueries.get_diagnosis_note)
    query.set_field("diagnosis_notes", DiagnosisQueries.get_diagnosis_notes)
    return query


def bind_mutation_type_to_resolvers():
    mutation = MutationType()
    mutation.set_field("createDiagnosis", DiagnosisMutations.create)
    mutation.set_field("updateDiagnosis", DiagnosisMutations.update)
    mutation.set_field("deleteDiagnosis", DiagnosisMutations.soft_delete)
    mutation.set_field("unarchiveDiagnosis", DiagnosisMutations.activate)
    mutation.set_field("archiveDiagnosis", DiagnosisMutations.deactivate)
    return mutation


# generate federated schema from type definitions, query, mutations and other objects
def generate_schema():
    type_defs = load_typedef_from_schema()
    query = bind_query_type_to_resolvers()
    mutation = bind_mutation_type_to_resolvers()
    schema = make_federated_schema(
        type_defs,
        [
            query,
            mutation,
            patient_federated_type,
            doctor_federated_type,
            diagnosis_federated_object,
        ],
    )
    return schema


# expose schema for imports from other modules
schema = generate_schema()
