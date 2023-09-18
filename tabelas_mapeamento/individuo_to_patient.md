| Descrição da entidade | Descrição do elemento | Tipo de dado | Mapeamento (FHIRPath) |
| :-------------------: | :-------------------: | :----------: | :-------------------: |
| Documento(s) do indivíduo | Identidade do sistema de terminologia do documento do indivíduo | string | Patient.identifier.where(system='https://rnds-fhir.saude.gov.br/NamingSystem/cpf').system |
| Documento(s) do indivíduo | Valor do documento do indivíduo no sistema de terminologia | string | Patient.identifier.where(system='https://rnds-fhir.saude.gov.br/NamingSystem/cpf').value |
| Registro em Uso | Indica se o registro desse indivíduo está em uso | boolean | Não será mapeado |
| Nome do Indivíduo | Nome do Indivíduo | string | O campo text é preenchido a partir do conteúdo extraído pelo FHIRPath Patient.name.where(use='official').text, sendo os campos "family" e "given" preenchidos com a extensão `data-absent-reason` |
| Meio de Contato | Meio de Contato | string | Patient.telecom.where(system='phone').value |
| Sexo | Sexo | code | Patient.gender |
| Data de Nascimento | Data de Nascimento | date | Patient.birthDate |
| Óbito | Indica se o indivíduo foi a óbito | boolean | Não será mapeado |
| Uso do Endereço | Uso do Endereço | code | Valor fixo `home` |
| Tipo de Endereço | Tipo de Endereço | code | Valor fixo `physical` |
| Endereço | Endereço com número, rua e complemento | string | Patient.address.where(use='home').line |
| Município | Município | string | Faz-se o lookup do valor extraído com o FHIRPath Patient.address.where(use='home').city utilizando o Code System `BRDivisaoGeograficaBrasil` |
| Estado | Estado | string | Faz-se o lookup do valor extraído com o FHIRPath Patient.address.where(use='home').state utilizando o Code System `BRDivisaoGeograficaBrasil` |
| CEP | CEP | string | Patient.address.where(use='home').postalCode |