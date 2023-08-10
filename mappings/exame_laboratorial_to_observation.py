from fhir.resources.observation import Observation
from fhirpathpy import evaluate
from utils.utils import lookup

def map_observation_results_laboratory(observation_rnds):
    print(f'Entrei no mapping com observation_rnds:{observation_rnds}')

    observation_metadata_profile = "https://ips-brasil.web.app/StructureDefinition-ObservationResultsLaboratoryBRIPS.html"

    observation_coding_code = evaluate(observation_rnds, "Observation.code.coding.code")[0]
    print(f'observation_coding_code:{observation_coding_code}')
    observation_coding_system = "https://loinc.org/" 

    observation_effectiveDateTime = evaluate(observation_rnds, "Observation.effectiveDateTime")[0]

    observation = {
        "resourceType" : "Observation",
        "status" : "final",
        "category" : [
            {
            "coding" : [
                {
                "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
                "code" : "laboratory"
                }
            ]
            }
        ],
        "code" : {
            "coding" : [
                {
                    "system" : observation_coding_system,
                    "code" : observation_coding_code
                }
            ]
        },
        "subject" : {
            "reference" : "TODO"
        },
        "effectiveDateTime" : observation_effectiveDateTime,
        "performer" : [
            {
                "reference" : "TODO"
            }
        ]
    }

    if len(evaluate(observation_rnds, "Observation.issued")) > 0:
        observation["issued"] = evaluate(observation_rnds, "Observation.issued")[0]
    if len(evaluate(observation_rnds, "Observation.method.text")) > 0:
        observation["method"] = {
            "text" : evaluate(observation_rnds, "Observation.issued")[0]
        }
    if len(evaluate(observation_rnds, "Observation.referenceRange")) > 0:
        observation["referenceRange"] = [
            {
                "text" : evaluate(observation_rnds, "Observation.referenceRange[0].text")[0]
            }
        ]

    return Observation(**observation).dict()