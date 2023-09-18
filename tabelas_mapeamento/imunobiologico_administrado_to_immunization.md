| Descrição da entidade | Descrição do elemento | Tipo de dado | Mapeamento (FHIRPath) |
| :-------------------: | :-------------------: | :----------: | :-------------------: |
| Estado da Administração do Imunobiológico | Indica o status atual do evento de imunização | code | Immunization.status |
| Imunobiológico Administrado | Identidade do sistema de terminologia do imunobiológico administrado | uri | Immunization.vaccineCode.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRImunobiologico').system |
| Imunobiológico Administrado | Código do imunobiológico administrado no sistema de terminologia | code | Immunization.vaccineCode.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRImunobiologico').code |
| Indivíduo | Indivíduo que recebeu o imunobiológico | string | Utiliza-se a url gerada para o recurso Patient no bundle |
| Data da Administração do Imunobiológico | Data ou data e hora que o imunobiológico foi administrado | dateTime | Immunization.occurrenceDateTime |
| Indicação da fonte do registro | Indica se o registro é de fonte própria (true) ou se é derivado de uma fonte externa (false) | boolean | Immunization.primarySource |
| Registro de Origem | Identidade do sistema de terminologia do registro de origem | uri | Immunization.reportOrigin.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRRegistroOrigem').system |
| Registro de Origem | Código do registro de origem no sistema de terminologia | code | Immunization.reportOrigin.coding.where(system = 'http://www.saude.gov.br/fhir/r4/CodeSystem/BRRegistroOrigem').code |
| Fabricante | Fabricante do imunobiológico | string | TODO:definir |
| Lote | Código do lote do imunobiológico | string | Immunization.lotNumber |
| Data de expiração do imunobiológico | Data de expiração do imunobiológico | date | Immunization.expirationDate |
| Local de Aplicação | Identidade do sistema de terminologia do local de aplicação do imunobiológico | uri | Immunization.site.coding.system |
| Local de Aplicação | Código do local de aplicação do imunobiológico no sistema de terminologia | code | Immunization.site.coding.code |
| Via de Administração | Identidade do sistema de terminologia da via de administração | uri | Immunization.route.coding.system |
| Via de Administração | Código da via de administração no sistema de terminologia | uri | Immunization.route.coding.code |
| Profissional Executante | Profissional Executante | string | Utiliza-se a url gerada para o recurso Practitioner no bundle |
| Dose do imunobiológico administrado | Dose do imunobiológico administrado | string | faz-se o lookup do display referente ao valor extraído pelo FHIRPath Immunization.protocolApplied.doseNumberString |