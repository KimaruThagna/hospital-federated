from django.db import models
from django.contrib.postgres.fields import JSONField
from utils.base_models import BaseModel
# Create your models here.

class Diagnosis(BaseModel):
    diagnosis = models.TextField(max_length=2000)
    consulting_doctor = JSONField()
    visiting_patient = JSONField()

    def __str__(self):
        return self.diagnosis