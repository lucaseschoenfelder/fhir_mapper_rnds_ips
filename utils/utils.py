import requests
from fhirpathpy import evaluate

def lookup(system, code):
    r = requests.get(f'{system}&code={code}')
    if r.status_code == 200:
        return evaluate(r.json(), "Parameters.parameter.where(name='display').valueString")
    else:
        print(f'Falha ao fazer lookup')
        return None