from fhir.resources.composition import Composition
from datetime import datetime
from babel.dates import format_datetime

def get_composition(patient_full_url, practitioner_full_url):

    datetime_now = datetime.now()

    composition = {
        "language" : "pt",
        #"versionNumber" : "1.0.0",
        #"identifier" : como preencher?,
        "status" : "final",
        "resourceType" : "Composition",
        "type" : {
            "coding" : [
                {
                    "system" : "http://loinc.org",
                    "code" : "60591-5",
                    "display" : "Patient summary Document"
                }
            ]
        },
        "subject" : [
            {
                "reference" : patient_full_url
            }
        ],
        "date" : datetime_now.strftime('%Y-%m-%dT%H:%M:%S%z'),
        "author" : [
            {
                "reference" : practitioner_full_url
            }
        ],
        "title" : f'Sumário Internacional do Paciente emitido em {format_datetime(datetime_now, "dd/MMMM/yyyy H:mm" , locale="pt")}',
        #"confidentiality" : "N",
        #"attester" : [
        #    {
        #        "mode" : "legal"
        #    }
        #],
        "custodian" : {
            "reference" : "00.394.544/0127-87"
        }
    }

    return Composition(**composition).dict()
