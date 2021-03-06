from typing import Any, Dict, Optional

from ariadne import convert_kwargs_to_snake_case
from diagnosis.models import Diagnosis
from django.db import transaction


class DiagnosisQueries:
    """
    Methods used to retrieve Diagnosiss data
    """

    @staticmethod
    def filter(queryset, filter_input):
        return queryset.filter(**filter_input)

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_diagnosis_note(_, info, uid):

        try:
            with transaction.atomic():
                return dict(
                    status=True,
                    object=Diagnosis.objects.get(uid=uid),
                )
        except Exception as e:
            return dict(status=False, error=f"An error as occurred {e}")

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_diagnosis_notes(_, info, filter_input: Optional[Dict[Any, Any]] = None):

        try:
            if filter_input is not None:
                return dict(
                    status=True,
                    object=DiagnosisQueries.filter(
                        Diagnosis.objects.all().not_deleted(), filter_input=filter_input
                    ),
                )
            else:
                return dict(status=True, object=Diagnosis.objects.all().not_deleted())

        except Exception as e:
            return dict(status=False, error=f"An error as occurred {e}")
