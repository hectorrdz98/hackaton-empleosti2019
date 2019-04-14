
import compareModules

def orderGeneral(vacancy, candidates, priorities):
    # print('\n\033[01m\033[93m--Entré a analisis orderGeneral()--\033[0m\n')

    finalPriorities = {
        'region': 1,
        'salary': 1,
        'skills': 1,
        'extra-skills': 1,
        'max-skills': 4,
        'last-jobs': 1,
        'current-job': 1,
        'type-job': 1,
        'type-job-percentaje': 0.75
    }

    for key,val in priorities.items():
        finalPriorities[key] = val

    results = {}

    # Compare lat - lon
    results = compareModules.orderByRegion(vacancy, candidates, finalPriorities['region'])
    # Compare salary
    results = compareModules.orderBySalary(vacancy, candidates, results, finalPriorities['salary'])
    # Compare skill
    results = compareModules.orderBySkill(vacancy, candidates, results, 
        [ finalPriorities['skills'], finalPriorities['extra-skills'], finalPriorities['max-skills'] ]
    )
    # Compare jobs
    results = compareModules.orderByJobs(vacancy, candidates, results, 
        [ finalPriorities['last-jobs'], finalPriorities['current-job'], finalPriorities['type-job'], finalPriorities['type-job-percentaje'] ]
    )

    return results