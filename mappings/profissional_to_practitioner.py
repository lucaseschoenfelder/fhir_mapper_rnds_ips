from fhir.resources.practitioner import Practitioner
from fhirpathpy import evaluate
from utils.utils import lookup

def map_practitioner(practitioner_rnds):
    identifier_system = None #TODO: adicionar evaluate pelo system
    identifier_value = None #TODO: adicionar evaluate pelo system

    name_text = evaluate(practitioner_rnds, "Practitioner.name.where(use='official').text")[0]

    practitioner = {
        "resourceType" : "Practitioner",
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
    }

    if len(evaluate(practitioner_rnds, "practitioner.address")) > 0:
        address_line = evaluate(practitioner_rnds, "Practitioner.address.where(use='home').line")
        address_city = evaluate(practitioner_rnds, "Practitioner.address.where(use='home').city")[0]
        address_state = evaluate(practitioner_rnds, "Practitioner.address.where(use='home').state")[0]
        address_postalCode = evaluate(practitioner_rnds, "Practitioner.address.where(use='home').postalCode")[0]

        # query for city
        query = lookup('https://oclapi2.gointerop.com/fhir/CodeSystem/$lookup?system=http://www.saude.gov.br/fhir/r4/CodeSystem/BRDivisaoGeograficaBrasil', address_city)
        if query is not None:
            address_city = query[0]

        #query for state
        query = lookup('https://oclapi2.gointerop.com/fhir/CodeSystem/$lookup?system=http://www.saude.gov.br/fhir/r4/CodeSystem/BRDivisaoGeograficaBrasil', address_state)
        if query is not None:
            address_state = query[0]
        
        #adicionar tipo logradouro

        practitioner["address"] = [
            {
                "use" : "home",
                "type" : "physical",
                "text" : " ".join(address_line),
                "city" : address_city,
                "state" : address_state,
                "postalCode" : address_postalCode
            }
        ]

    if len(evaluate(practitioner_rnds, "Practitioner.telecom")) > 0:
        telecom_value = evaluate(practitioner_rnds, "Practitioner.telecom.where(system='http://hl7.org/fhir/ValueSet/contact-point-system').value")[0]
        #telecom_use = evaluate(practitioner_rnds, "Practitioner.telecom.where(system='http://hl7.org/fhir/ValueSet/contact-point-system').use")[0]

        practitioner["telecom"] = [
            {
                "system" : "phone",
                "value" : telecom_value
            }
        ]
    
    return Practitioner(**practitioner).dict()