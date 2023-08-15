from fhir.resources.specimen import specimen
from fhirpathpy import evaluate
from utils.utils import lookup

def map_specimen(specimen_rnds):

    type_coding_system = evaluate(specimen_rnds, "Specimen.type.coding.where(system = 'https://rnds-fhir.saude.gov.br/CodeSystem/BRTipoAmostraGAL').system") #TODO precisa mudar pra LOINC?
    type_coding_code =  evaluate(specimen_rnds, "Specimen.type.coding.where(system = 'https://rnds-fhir.saude.gov.br/CodeSystem/BRTipoAmostraGAL').code")

    specimen = {
        "resourceType" : "Specimen",
        "type" : {
            "coding" : [
                "system" : type_coding_system,
                "code" : type_coding_code
            ]
        }
    }    
    return Specimen(**specimen).dict()