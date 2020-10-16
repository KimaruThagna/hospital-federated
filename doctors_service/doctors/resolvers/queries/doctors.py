from typing import Any, Dict, Optional

from ariadne import convert_kwargs_to_snake_case
from doctors_service.doctors.models import Doctor


class DoctorsQueries:
    """
    Methods used to retrieve Doctors data
    """

    @staticmethod
    def filter(queryset, filter_input):
        return queryset.filter(**filter_input)

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_doctor(_, info, uid):
        try:
            return dict(status=True, object=Doctor.objects.get(uid=uid))
        except Exception as e:
            return dict(status=False, error=f"An error as occurred {e}")

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_doctors(_, info, filter_input: Optional[Dict[Any, Any]] = None):

        try:
            if filter_input is not None:
                return dict(
                    status=True,
                    object=DoctorsQueries.filter(
                        Doctor.objects.all().not_deleted(), filter_input=filter_input
                    ),
                )
            else:
                return dict(status=True, object=Doctor.objects.all().not_deleted())

        except Exception as e:
            return dict(status=False, error=f"An error as occurred {e}")
