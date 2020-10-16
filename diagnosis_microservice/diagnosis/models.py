import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from utils.base_models import BaseModel


class Diagnosis(BaseModel):
    diagnosis = models.TextField(max_length=2000)
    consulting_doctor = models.UUIDField(editable=False)
    visiting_patient = models.UUIDField(editable=False)

    def __str__(self):
        return self.diagnosis
