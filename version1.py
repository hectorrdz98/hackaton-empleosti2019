import json
import analisis

# Colors for terminal

colors = {
    'reset': '\033[0m',
    'green': '\033[32m',
    'red': '\033[31m',
    'yellow': '\033[93m',
    'cyan': '\033[36m',
    'orange': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'pink': '\033[95m',
    'bold': '\033[01m',
    'underline': '\033[04m',
}

import os           
os.system('color')          # Activate color mode in terminal

def printJSON(json2Print):
    print(json.dumps(json2Print, indent=4, sort_keys=True))


# Load vacancy

with open('vacante.json', 'r', encoding="utf8") as f:
    vacante = json.load(f)[15]


# Load candidates

with open('candidatos.json', 'r', encoding="utf8") as f:
    candidatos = json.load(f)


# Priorities

priorities = {
    'region': 1,
    'salary': 1,
    'skills': 1,
    'extra-skills': 0.5,
    'max-skills': 4,
    'last-jobs': 0,
    'current-job': 20,
    'type-job': 1,
    'type-job-percentaje': 0.6
}

results = analisis.orderGeneral(vacante, candidatos, priorities)

print('\n{}{}Resultados{}\n'.format(
    colors['bold'], colors['blue'], colors['reset']
))
for candId, result in results.items():
    print('{}: {}'.format(candId, result['dist']))

#print('\n{}{}Resultados{}\n'.format(
#    colors['bold'], colors['blue'], colors['reset']
#))

#printJSON(results)

# Show JSONs
"""
print('\n{}{}Vacante{}\n'.format(
    colors['bold'], colors['blue'], colors['reset']
))

printJSON(vacante)

print('\n\n{}{}Candidatos{}\n'.format(
    colors['bold'], colors['blue'], colors['reset']
))

printJSON(candidatos)
"""

