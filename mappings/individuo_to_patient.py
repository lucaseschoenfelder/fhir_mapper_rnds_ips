from fhir.resources.patient import Patient
from fhirpathpy import evaluate
from utils.utils import lookup

def map_patient(patient_rnds):
    # adicionar query CNS
    identifier_system = evaluate(patient_rnds, "Patient.identifier.where(system='https://rnds-fhir.saude.gov.br/NamingSystem/cpf').system")[0]
    identifier_value = evaluate(patient_rnds, "Patient.identifier.where(system='https://rnds-fhir.saude.gov.br/NamingSystem/cpf').value")[0]

    name_text = evaluate(patient_rnds, "Patient.name.where(use='official').text")[0]

    gender = evaluate(patient_rnds, "Patient.gender")[0]
    
    birth_date = evaluate(patient_rnds, "Patient.birthDate")[0]

    patient = {
        "resourceType" : "Patient",
        "identifier" : [
            {
                "system" : identifier_system,
                "value" : identifier_value
            }
        ],
        "name" : [
            {
                "text" : name_text,
                "_family" : {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                            "valueCode": "unknown"
                        }
                    ]
                },
                "_given" : [
                    {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                                "valueCode": "unknown"
                            }
                        ]
                    }
                ]
            }
        ],
        "gender" : gender,
        "birthDate" : birth_date,
        "generalPractitioner" : [
            {
                "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                            "valueCode": "unknown"
                        }
                    ]
            }
        ]
    }
    
    if len(evaluate(patient_rnds, "Patient.address")) > 0:
        address_line = evaluate(patient_rnds, "Patient.address.where(use='home').line")
        address_city = evaluate(patient_rnds, "Patient.address.where(use='home').city")[0]
        address_state = evaluate(patient_rnds, "Patient.address.where(use='home').state")[0]
        address_postalCode = evaluate(patient_rnds, "Patient.address.where(use='home').postalCode")[0]

        # query for city
        query = lookup('https://oclapi2.gointerop.com/fhir/CodeSystem/$lookup?system=http://www.saude.gov.br/fhir/r4/CodeSystem/BRDivisaoGeograficaBrasil', address_city)
        if query is not None:
            address_city = query[0]

        #query for state
        query = lookup('https://oclapi2.gointerop.com/fhir/CodeSystem/$lookup?system=http://www.saude.gov.br/fhir/r4/CodeSystem/BRDivisaoGeograficaBrasil', address_state)
        if query is not None:
            address_state = query[0]
        
        #adicionar tipo logradouro

        patient["address"] = [
            {
                "use" : "home",
                "type" : "physical",
                "text" : " ".join(address_line),
                "city" : address_city,
                "state" : address_state,
                "postalCode" : address_postalCode
            }
        ]
    
    if len(evaluate(patient_rnds, "Patient.telecom")) > 0:
        telecom_value = evaluate(patient_rnds, "Patient.telecom.where(system='phone').value")[0]
        telecom_use = evaluate(patient_rnds, "Patient.telecom.where(system='phone').use")[0]

        patient["telecom"] = [
            {
                "system" : "phone",
                "value" : telecom_value
            }
        ]


    return Patient(**patient).dict()