import pandas as pd
from diagnosis.models import *
from django.conf import settings
from os.path import join
import json
from django.core.management.base import BaseCommand

def prefill_diagnosis(filename):
    data = pd.read_csv(filename)
    # convert data to a list of dictionaries for easy data entry
    diagnosis_records = data.T.to_dict().values()
    for record in diagnosis_records:
        record["visiting_patient"] = json.loads(record["visiting_patient"])
        record["consulting_doctor"] = json.loads(record["consulting_doctor"])


    try:
        for record in diagnosis_records:
            Diagnosis.objects.create(**record)
            print(f'added diagnosis record')
    except Exception as e:
        print(f"DB prefill process failed due to {e}")

#prefill_diagnosis('/home/macbuntu/PycharmProjects/diagnosis_microservice/postgres_prefill/diagnosis_list.csv')
class Command(BaseCommand):

    def handle(self, *args, **options):
        prefill_diagnosis(join(settings.BASE_DIR,'postgres_prefill/diagnosis_list.csv'))