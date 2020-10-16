import csv
from os.path import join

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction
from doctors.models import *


def prefill_doctors(filename):
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for record in reader:
            try:
                try:
                    _ = Doctor.objects.get(license_number=record["license_number"])
                except Doctor.DoesNotExist:
                    with transaction.atomic():
                        Doctor.objects.create(**record)
                    print(
                        f'added doctors record for {record["last_name"]} in the {record["specialization"]} department'
                    )
            except IntegrityError:
                print(
                    f'doctors record for {record["last_name"]} in the {record["specialization"]} '
                    f"department already exists"
                )
            except Exception as e:
                print(f"DB prefill process failed due to {e}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        prefill_doctors(join(settings.BASE_DIR, "postgres_prefill/doctor_list.csv"))
