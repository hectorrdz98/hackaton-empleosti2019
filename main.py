from flask import Flask, request
import requests
import json
import analisis
import re

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola!!!"

@app.route('/getCandidates')
def getCandidates():
    vacancy_id = request.args.get('id')
    vacancy_num = int(request.args.get('take'))

    useLocalVacancies = False
    useLocalCandidates = True

    if useLocalVacancies:
        with open('vacante.json', 'r', encoding="utf8") as f:
            vacantes = json.load(f)
            for vacante in vacantes:
                if int(vacante['id']) == int(vacancy_id):
                    break
    
    else:
        r = requests.get('https://empleosti.com.mx/api/v2/vacancies?token=HrYKX42Ix0&vacancy_id={}'.format(vacancy_id))
        vacante = r.json()[0]

    print('\nVacancy id: %s\n' % vacancy_id)
    # print(vacante)

    if useLocalCandidates:
        with open('candidatos.json', 'r', encoding="utf8") as f:
            candidatos = json.load(f)
    else:
        r = requests.get('https://empleosti.com.mx/api/v2/candidates?token=HrYKX42Ix0')
        candidatos = r.json()

    # Priorities

    # print(re.sub(r'\s+', '', request.args.get('priorities')))
    priorities = json.loads(re.sub(r'\s+', '', request.args.get('priorities')))
    # print(priorities)

    """
    priorities = {
        'region': 10,
        'salary': 10,
        'skills': 5,
        'extra-skills': 1,
        'max-skills': 4,
        'last-jobs': 0.3,
        'current-job': 0.5,
        'type-job': 50,
        'type-job-percentaje': 0.75
    }
    """

    results = analisis.orderGeneral(vacante, candidatos, priorities)

    # print()
    # print(results)
    # print()

    candidates = []

    for key,val in results.items():
        for candidato in candidatos:
            if candidato['id'] == key:
                candidates.append(candidato)
                break


    return json.dumps(candidates[:vacancy_num])

if __name__ == "__main__":
    app.run(host='localhost', port=7711, debug=True)