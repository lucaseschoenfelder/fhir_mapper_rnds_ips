import requests
from fhirpathpy import evaluate

def lookup(system, code):
    r = requests.get(f'{system}&code={code}')
    if r.status_code == 200:
        return evaluate(r.json(), "Parameters.parameter.where(name='display').valueString")
    else:
        print(f'Falha ao fazer lookup')
        return None

mock_patient_rnds = {
  "resourceType": "Patient",
  "id": "dfc68402-7e80-4365-97df-52c4c870a159",
  "meta": {
    "profile": [
      "https://rnds-fhir.saude.gov.br/StructureDefinition/BRIndividuo-1.0"
    ]
  },
  "extension": [
    {
      "extension": [
        {
          "url": "relationship",
          "valueCode": "MTH"
        },
        {
          "url": "parent",
          "valueHumanName": {
            "use": "official",
            "text": "MARILIA FARES DA ROCHA ALVES"
          }
        }
      ],
      "url": "https://rnds-fhir.saude.gov.br/StructureDefinition/BRParentesIndividuo-1.0"
    },
    {
      "extension": [
        {
          "url": "relationship",
          "valueCode": "FTH"
        },
        {
          "url": "parent",
          "valueHumanName": {
            "use": "official",
            "text": "JURACY ALVES"
          }
        }
      ],
      "url": "https://rnds-fhir.saude.gov.br/StructureDefinition/BRParentesIndividuo-1.0"
    },
    {
      "extension": [
        {
          "url": "race",
          "valueCodeableConcept": {
            "coding": [
              {
                "system": "https://rnds-fhir.saude.gov.br/CodeSystem/BRRacaCor-1.0",
                "code": "01"
              }
            ]
          }
        }
      ],
      "url": "https://rnds-fhir.saude.gov.br/StructureDefinition/BRRacaCorEtnia-1.0"
    },
    {
      "url": "https://rnds-fhir.saude.gov.br/StructureDefinition/BRPais-1.0",
      "valueCodeableConcept": {
        "coding": [
          {
            "system": "https://rnds-fhir.saude.gov.br/CodeSystem/BRPais",
            "code": "10"
          }
        ]
      }
    }
  ],
  "identifier": [
    {
      "use": "official",
      "type": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code": "TAX"
          }
        ]
      },
      "system": "https://rnds-fhir.saude.gov.br/NamingSystem/cpf",
      "value": "12345678900"
    }
  ],
  "active": True,
  "name": [
    {
      "use": "official",
      "text": "GABRIELA INACIO ALVES"
    }
  ],
  "gender": "female",
  "birthDate": "1976-09-15",
  "deceasedBoolean": False,
  "address": [
    {
      "use": "home",
      "type": "physical",
      "line": [
        "081",
        "SQN  BLOCO M",
        "604",
        "APARTAMENTO",
        "ASA NORTE"
      ],
      "city": "315780",
      "state": "53",
      "postalCode": "70752130"
    }
  ]
}

mock_practitioner_rnds = {
  "resourceType": "Practitioner",
  "id": "dfc68402-7e80-4365-97df-52c4c870a159",
  "meta": {
    "profile": [
      "https://rnds-fhir.saude.gov.br/StructureDefinition/BRIndividuo-1.0"
    ]
  },
  "extension": [
    {
      "extension": [
        {
          "url": "relationship",
          "valueCode": "MTH"
        },
        {
          "url": "parent",
          "valueHumanName": {
            "use": "official",
            "text": "MARILIA FARES DA ROCHA ALVES"
          }
        }
      ],
      "url": "https://rnds-fhir.saude.gov.br/StructureDefinition/BRParentesIndividuo-1.0"
    },
    {
      "extension": [
        {
          "url": "relationship",
          "valueCode": "FTH"
        },
        {
          "url": "parent",
          "valueHumanName": {
            "use": "official",
            "text": "JURACY ALVES"
          }
        }
      ],
      "url": "https://rnds-fhir.saude.gov.br/StructureDefinition/BRParentesIndividuo-1.0"
    },
    {
      "extension": [
        {
          "url": "race",
          "valueCodeableConcept": {
            "coding": [
              {
                "system": "https://rnds-fhir.saude.gov.br/CodeSystem/BRRacaCor-1.0",
                "code": "01"
              }
            ]
          }
        }
      ],
      "url": "https://rnds-fhir.saude.gov.br/StructureDefinition/BRRacaCorEtnia-1.0"
    },
    {
      "url": "https://rnds-fhir.saude.gov.br/StructureDefinition/BRPais-1.0",
      "valueCodeableConcept": {
        "coding": [
          {
            "system": "https://rnds-fhir.saude.gov.br/CodeSystem/BRPais",
            "code": "10"
          }
        ]
      }
    }
  ],
  "identifier": [
    {
      "use": "official",
      "type": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code": "TAX"
          }
        ]
      },
      "system": "https://rnds-fhir.saude.gov.br/NamingSystem/cpf",
      "value": "12345678900"
    }
  ],
  "active": True,
  "name": [
    {
      "use": "official",
      "text": "GABRIELA INACIO ALVES"
    }
  ],
  "gender": "female",
  "birthDate": "1976-09-15",
  "address": [
    {
      "use": "home",
      "type": "physical",
      "line": [
        "081",
        "SQN  BLOCO M",
        "604",
        "APARTAMENTO",
        "ASA NORTE"
      ],
      "city": "315780",
      "state": "53",
      "postalCode": "70752130"
    }
  ],
	  "telecom": [
  	{
    	"system": "http://hl7.org/fhir/ValueSet/contact-point-system",
        "value" : "41989023866"
    }
  ],
	"qualification" : [
		{
			"code" : {
				"coding" : {
						"system" : "algum_sistema",
						"code" : "algum_codigo"
				}
			}
		} 
	]
}