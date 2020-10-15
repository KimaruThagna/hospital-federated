import csv
from os.path import join

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction
from patient.models import *


def prefill_patients(filename):
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for record in reader:
            try:
                try:
                    _ = Patient.objects.get(patient_number=record["patient_number"])
                except Patient.DoesNotExist:
                    with transaction.atomic():
                        Patient.objects.create(**record)
                    print(f'added patients record for {record["last_name"]}')
            except IntegrityError:
                print(f'patients record for {record["last_name"]} already exists')
            except Exception as e:
                print(f"DB prefill process failed due to {e}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        prefill_patients(join(settings.BASE_DIR, "postgres_prefill/patient_list.csv"))
