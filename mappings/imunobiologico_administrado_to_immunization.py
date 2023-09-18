from fhir.resources.immunization import Immunization
from fhirpathpy import evaluate
from utils.utils import lookup, translate

def map_immunization(immunization_rnds, patient_full_url):

    immunization_status = evaluate(immunization_rnds, "Immunization.status")[0]

    immunization_vaccineCode_coding_system = evaluate(immunization_rnds, "Immunization.vaccineCode.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRImunobiologico').system")[0]
    immunization_vaccineCode_coding_value = evaluate(immunization_rnds, "Immunization.vaccineCode.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRImunobiologico').code")[0]

    # translate code
    translated_vaccine_code = translate(immunization_vaccineCode_coding_system, immunization_vaccineCode_coding_value)
    print(f'translated_vaccine_code:{translated_vaccine_code}')
    immunization_vaccineCode_coding_system = translated_vaccine_code["system"]
    immunization_vaccineCode_coding_value = translated_vaccine_code["code"] 

    immunization_occurenceDateTime = evaluate(immunization_rnds, "Immunization.occurrenceDateTime")[0]

    immunization_lotNumber = evaluate(immunization_rnds, "Immunization.lotNumber")[0]
    immunization_protocolApplied_doseNumberString = evaluate(immunization_rnds, "Immunization.protocolApplied.doseNumberString")[0]

    query = lookup('https://oclapi2.gointerop.com/fhir/CodeSystem/$lookup?system=http://www.saude.gov.br/fhir/r4/CodeSystem/BRDose', immunization_protocolApplied_doseNumberString)
    if query is not None:
        immunization_protocolApplied_doseNumberString = query[0]

    immunization = {
        "resourceType" : "Immunization",
        "status" : immunization_status,
        "vaccineCode" : {
            "coding" : [
                {
                    "system" : immunization_vaccineCode_coding_system,
                    "code" : immunization_vaccineCode_coding_value,
                }
            ]
        },
        "patient" : {
            "reference" : patient_full_url
        },
        "occurrenceDateTime" : immunization_occurenceDateTime,
        "lotNumber" : immunization_lotNumber,
        "protocolApplied" : [
            {
                "doseNumberString" : immunization_protocolApplied_doseNumberString
            }
        ]
    }

    # lookup
    query = lookup('https://oclapi2.gointerop.com/fhir/CodeSystem/$lookup?system=http://snomed.info/sct', immunization_vaccineCode_coding_value)
    if query is not None:
        print(f'query:{translated_vaccine_code}')
        immunization_vaccineCode_coding_display = query[0]
        immunization["vaccineCode"]["coding"][0]["display"] = immunization_vaccineCode_coding_display

    if len(evaluate(immunization_rnds, "Immunization.primarySource")) > 0:
        immunization_primarySource = evaluate(immunization_rnds, "Immunization.primarySource")[0]

        immunization["primarySource"] = immunization_primarySource
    
    if len(evaluate(immunization_rnds, "Immunization.reportOrigin.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRRegistroOrigem')")) > 0:
        immunization_reportOrigin_coding_system = evaluate(immunization_rnds, "Immunization.reportOrigin.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRRegistroOrigem').system")[0]
        immunization_reportOrigin_coding_code = evaluate(immunization_rnds, "Immunization.reportOrigin.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRRegistroOrigem').code")[0]

        immunization["reportOrigin"] = {
            "coding" : {
                "system" : immunization_reportOrigin_coding_system,
                "code" : immunization_reportOrigin_coding_code
            }
        }
    
    if len(evaluate(immunization_rnds, "Immunization.expirationDate")) > 0:
        immunization_expirationDate = evaluate(immunization_rnds, "Immunization.expirationDate")[0]

        immunization["expirationDate"] = immunization_expirationDate

    if len(evaluate(immunization_rnds, "Immunization.site.coding.system")) > 0:
        immunization_site_coding_system = evaluate(immunization_rnds, "Immunization.site.coding.system")[0] #TODO: trocar pelo system quando soubermos qual é
        immunization_site_coding_value = evaluate(immunization_rnds, "Immunization.site.coding.code")[0] #TODO: trocar pelo system quando soubermos qual é
    
        immunization["site"] = {
            "coding" : {
                "system" : immunization_site_coding_system,
                "value" : immunization_site_coding_code
            }
        } 
    
    if len(evaluate(immunization_rnds, "Immunization.route.coding.system")) > 0:
        immunization_route_coding_system = evaluate(immunization_rnds, "Immunization.route.coding.system")[0] #TODO: trocar pelo system quando soubermos qual é
        immunization_route_coding_value = evaluate(immunization_rnds, "Immunization.route.coding.code")[0] #TODO: trocar pelo system quando soubermos qual é
    
        immunization["route"] = {
            "coding" : {
                "system" : immunization_route_coding_system,
                "value" : immunization_route_coding_code
            }
        }


    return immunization