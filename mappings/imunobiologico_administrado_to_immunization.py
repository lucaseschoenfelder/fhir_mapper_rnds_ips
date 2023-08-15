from fhir.resources.immunization import Immunization
from fhirpathpy import evaluate
from utils.utils import lookup

def map_immunization(immunization_rnds, patient_full_url):

    immunization_status = evaluate(immunization_rnds, "Immunization.status")[0]

    immunization_vaccineCode_coding_system = evaluate(immunization_rnds, "Immunization.vaccineCode.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRImunobiologico').system")[0]
    immunization_vaccineCode_coding_value = evaluate(immunization_rnds, "Immunization.vaccineCode.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRImunobiologico').code")[0]

    immunization_occurenceDateTime = evaluate(immunization_rnds, "Immunization.occurrenceDateTime")[0]

    #immunization_protocol_applied = evaluate(immunization_rnds, "Immunization.protocolApplied.doseNumberString")

    immunization = {
        "resourceType" : "Immunization",
        "status" : immunization_status,
        "vaccineCode" : {
            "coding" : [
                {
                    "system" : immunization_vaccineCode_coding_system,
                    "code" : immunization_vaccineCode_coding_value
                }
            ]
        },
        "patient" : {
            "reference" : patient_full_url
        },
        "occurrenceDateTime" : immunization_occurenceDateTime
        
    }

    if len(evaluate(immunization_rnds, "Immunization.site.coding.system")) > 0:
        immunization_site_coding_system = evaluate(immunization_rnds, "Immunization.site.coding.system")[0] #TODO: trocar pelo system quando soubermos qual é
        immunization_site_coding_value = evaluate(immunization_rnds, "Immunization.site.coding.code")[0] #TODO: trocar pelo system quando soubermos qual é
    
        immunization["site"] = {
            "coding" : {
                "system" : immunization_site_coding_system,
                "value" : immunization_site_coding_code
            }
        }


    return Immunization(**immunization).dict()