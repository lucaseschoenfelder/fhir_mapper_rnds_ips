from fhir.resources.composition import Composition
from datetime import datetime
from babel.dates import format_datetime

def get_composition(patient_full_url, practitioner_full_url):

    datetime_now = datetime.now()

    composition = {
        "language" : "pt",
        "versionNumber" : "1.0.0",
        #"identifier" : como preencher? uuid,
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
        "confidentiality" : "N",
        "attester" : [
            {
                "mode" : "legal"
            }
        ],
        "custodian" : {
            "reference" : "00.394.544/0127-87"
        },
        "section" : [
            {
                "title" : f'Seção de Medicamentos do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "10160-0"
                        }
                    ]
                },
                #author : [
                    #{
                    #    "reference" : #o que vier do RAC
                    #}
                #],
                #text: , #o que vier do RAC
                #"orderedBy" : event-date # o que vier do RAC
                #"entry" : [
                #    {
                #        "reference" : "MedicationStatementBRIPS" # como fica essa reference?
                #    }
                #]
            },
            {
                "title" : f'Seção de Alergias/Reações Adversas do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "48765-2"
                        }
                    ]
                },
                #author : [
                    #{
                    #    "reference" : #o que vier do RAC
                    #}
                #],
                #"entry" : [
                #    {
                #        "reference" : "AllergyIntoleranceBRIPS" # como fica essa reference?
                #    }
                #]
            },
            {
                "title" : f'Seção de Problemas do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "11450-4"
                        }
                    ]
                },
                #author : [
                    #{
                    #    "reference" : #o que vier do RAC
                    #}
                #],
                #text: , #o que vier do RAC
                #"orderedBy" : event-date # o que vier do RAC
                #"entry" : [
                #    {
                #        "reference" : "ConditionBRIPS" # como fica essa reference?
                #    }
                #]
            },
            {
                "title" : f'Seção de Procedimentos do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "47519-4"
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            },
            {
                "title" : f'Seção de Imunobiológicos Administrados do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "11369-6"
                        }
                    ]
                },
                #author : [
                    #{
                    #    "reference" : #o que vier do RAC
                    #}
                #],
                #text: , #o que vier do RAC
                #"orderedBy" : event-date # o que vier do RAC
                #"entry" : [
                #    {
                #        "reference" : "ImmunizationBRIPS" # como fica essa reference?
                #    }
                #]
            },
            {
                "title" : f'Seção de Dispositivos Médicos do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "47519-4" #mesmo valor que o de procedimentos?
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            },
            {
                "title" : f'Seção de Resultados do Sumário Internacional do Paciente”',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "30954-2"
                        }
                    ]
                },
                #author : [
                    #{
                    #    "reference" : #o que vier do RAC
                    #}
                #],
                #text: , #o que vier do RAC
                #"orderedBy" : event-date # o que vier do RAC
                #"entry" : [
                #    {
                #        "reference" : "ObservationResultsBRIPS" # como fica essa reference?
                #    },
                #    {
                #        "reference" : "DiagnosticReportBRIPS" # como fica essa reference?
                #    },
                #]
            },
            {
                "title" : f'Seção de Sinais Vitais do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "8716-3"
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            },
            {
                "title" : f'Seção de História Pregressa do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "11348-0"
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            },
            {
                "title" : f'Seção de Status Funcional do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "47420-5"
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            },
            {
                "title" : f'Seção de Plano de Cuidado do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "18776-5"
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            },
            {
                "title" : f'Seção de História Social do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "29762-2"
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            },
            {
                "title" : f'Seção de História Obstétrica do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "10162-6"
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            },
            {
                "title" : f'Seção de Diretivas Antecipadas de Vontade do Sumário Internacional do Paciente',
                "code" : {
                    "coding" : [
                        {
                            "system" : "http://loinc.org",
                            "code" : "42348-3"
                        }
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                        "valueCode": "unknown"
                    }
                ]
            }
        ]
    }

    return composition
