import csv
import json
from os.path import join

from diagnosis.models import *
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction


def prefill_diagnosis(filename):
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for record in reader:
            record["visiting_patient"] = json.loads(record["visiting_patient"])
            record["consulting_doctor"] = json.loads(record["consulting_doctor"])
            try:
                with transaction.atomic():
                    Diagnosis.objects.create(**record)
                print(f"added diagnosis record")
            except IntegrityError:
                print(f"diagnosis record already exists")
            except Exception as e:
                print(f"DB prefill process failed due to {e}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        prefill_diagnosis(
            join(settings.BASE_DIR, "postgres_prefill/diagnosis_list.csv")
        )
