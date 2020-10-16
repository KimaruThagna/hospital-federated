from os.path import dirname, join

from ariadne import MutationType, QueryType, gql, load_schema_from_path
from ariadne.contrib.federation import make_federated_schema
from doctors.resolvers.federation.doctors import doctor_federated_object
from doctors.resolvers.mutations.doctors import *
from doctors.resolvers.queries.doctors import *


def load_typedef_from_schema():
    type_def = load_schema_from_path(join(dirname(dirname(__file__)), "./gql"))
    type_defs = gql(type_def)
    return type_defs


# query type and its fields resolvers
def bind_query_type_to_resolvers():
    query = QueryType()
    query.set_field("doctor", DoctorsQueries.get_doctor)
    query.set_field("doctors", DoctorsQueries.get_doctors)
    return query


def bind_mutation_type_to_resolvers():
    mutation = MutationType()
    mutation.set_field("createDoctor", DoctorsMutations.create)
    mutation.set_field("updateDoctor", DoctorsMutations.update)
    mutation.set_field("deleteDoctor", DoctorsMutations.soft_delete)
    mutation.set_field("activateDoctor", DoctorsMutations.activate)
    mutation.set_field("deactivateDoctor", DoctorsMutations.deactivate)
    return mutation


# generate federated schema from type definitions, query, mutations and other objects
def generate_schema():
    type_defs = load_typedef_from_schema()
    query = bind_query_type_to_resolvers()
    mutation = bind_mutation_type_to_resolvers()
    schema = make_federated_schema(
        type_defs, [query, mutation, doctor_federated_object]
    )
    return schema


# expose schema for imports from other modules
schema = generate_schema()
