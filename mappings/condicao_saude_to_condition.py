from fhir.resources.condition import Condition
from fhirpathpy import evaluate
from utils.utils import lookup

def map_condition_condicaoSaude(condition_rnds, subject_full_url):
    condition_code_coding_system = evaluate(condition_rnds, "Condition.code.coding.where(system = 'https://rnds-fhir.saude.gov.br/CodeSystem/BRTerminologiaSuspeitaDiagnostica').system")[0]
    condition_code_coding_code = evaluate(condition_rnds, "Condition.code.coding.where(system = 'https://rnds-fhir.saude.gov.br/CodeSystem/BRTerminologiaSuspeitaDiagnostica').code")[0]

    condition_subject = evaluate(condition_rnds, "Condition.subject.identifier[0].value")[0]

    condition = {
        "resourceType" : "Condition",
        "clinicalStatus" : {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                    "valueCode": "unknown"
                }
            ]
        },
        "code" : {
            "coding" : [
                {
                    "system" : condition_code_coding_system,
                    "code" : condition_code_coding_code
                }
            ]
        },
        "subject" : {
            "reference" : subject_full_url
        }
    }

    if len(evaluate(condition_rnds, "Condition.verificationStatus.coding.code")) > 0:
        condition_verificationStatus_code = evaluate(condition_rnds, "Condition.verificationStatus.coding.code")[0] # TODO: confirmar preenchimento desse campo
        condition["verificationStatus"] = {
            "coding" : [
                {
                    "code" : condition_verificationStatus_code
                }
            ]
        }

    return Condition(**condition).dict()