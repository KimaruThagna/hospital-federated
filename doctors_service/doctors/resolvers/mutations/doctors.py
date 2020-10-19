from ariadne import convert_kwargs_to_snake_case
from django.db import transaction
from doctors.models import Doctor


class DoctorsMutations:
    """
    Mutation methods to perform creation updates and deletion in the Doctors model
    """

    def __init__(self):
        pass

    @staticmethod
    def create(_, info, creation_input):

        try:
            with transaction.atomic():

                return dict(status=True, object=Doctor.objects.create(**creation_input))
        except Exception as e:
            return dict(status=False, error=f"An error occurred {e}")

    @staticmethod
    def update(_, info, update_input):

        try:
            with transaction.atomic():
                doctor = Doctor.objects.get(uid=update_input.get("uid"))
                Doctor.objects.filter(uid=update_input.pop("uid")).update(
                    **update_input
                )
                return dict(status=True, object=doctor)
        except Exception as e:
            return dict(status=False, error=f"An error occurred {e}")

    @staticmethod
    def soft_delete(_, info, uid):

        try:
            with transaction.atomic():
                record = Doctor.objects.get(uid=uid)
                record.soft_delete()
                return dict(status=True, object=record)
        except Exception as e:
            return dict(status=False, error=f"An error occurred: {e}")

    @staticmethod
    @convert_kwargs_to_snake_case
    def activate(_, info, uid):

        try:
            with transaction.atomic():
                record = Doctor.objects.get(uid=uid)
                record.activate()
                return dict(status=True, object=record)
        except Exception as e:
            return dict(status=False, error=f"An error occurred: {e}")

    @staticmethod
    @convert_kwargs_to_snake_case
    def deactivate(_, info, uid):

        try:
            with transaction.atomic():
                record = Doctor.objects.get(uid=uid)
                record.deactivate()
                return dict(status=True, object=record)
        except Exception as e:
            return dict(status=False, error=f"An error occurred: {e}")
