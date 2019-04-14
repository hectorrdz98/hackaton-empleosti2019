import requests
import math
import json
import re
import pickle
from datetime import datetime
from difflib import SequenceMatcher

# We get the lat and lon of a region by its name, then we calculate the
# distance between each candidate location with the vacancy location
# and divide them between the biggest one, so we get values between
# [ 0, 1 ] * priority
def orderByRegion(vacancy, candidates, priority):
    print('\033[01m\033[35m--Entré a compareModules orderByRegion()--\033[0m\n')

    # print('Vacancy region_name: {}'.format(vacancy['region_name']))
    # print('Vacancy region_id: {}'.format(vacancy['region_id']))
    
    file = open('latlon.data', 'rb')
    latlon = pickle.load(file)
    # print(latlon)

    # Comparing phase

    distances = []
    maxDist = 0

    for candidate in candidates:
        # print('Comparing region "{}" with "{}"'.format( vacancy['region_name'],  candidate['region_name']))

        # Approximate radius of earth in km
        R = 6373.0

        lat1 = math.radians( latlon[vacancy['region_name']]['lat'] )
        lon1 = math.radians( latlon[vacancy['region_name']]['lng'] )
        lat2 = math.radians( latlon[candidate['region_name']]['lat'] )
        lon2 = math.radians( latlon[candidate['region_name']]['lng'] )

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c

        if distance > maxDist:
            maxDist = distance

        distances.append({
            'id': candidate['id'],
            'dist': distance
        })

        # print('Distancia: {}'.format(distance))

    # distances = json.dumps()

    distances = order(distances)

    distancesNew = {}

    if maxDist > 0:
        # distances = [ { 'id': dist['id'], 'dist': dist['dist'] / maxDist } for dist in distances ]
        for dist in distances:
            distancesNew[dist['id']] = {
                'dist': priority - ((dist['dist'] / maxDist)*priority)
            }

    # distances = json.dumps(distances)

    # print('\nDistancias normalizadas:\n\n{}'.format(distances))
    # print('Distancias normalizadas:\n\n{}\n'.format(distancesNew))

    return distancesNew

# We get the salary range and put
# 0 if the min candidate salary range is greater than the max vacancy salary range
# 0.5 if the min candidate salary range is between the max and min vacancy salary range
# 1 if the min candidate salary range is lower than the min vacancy salary range
# Then we multiply by priority
def orderBySalary(vacancy, candidates, results, priority):
    print('\033[01m\033[35m--Entré a compareModules orderBySalary()--\033[0m\n')
    
    # print('Salario de la vacante:')

    if vacancy['salary'] != '':
        vacSalary = [ int(str(val.split(',')[0]) + str(val.split(',')[1])) for val in re.findall(r'(\d+\,\d+)', vacancy['salary']) ]
    else:
        vacSalary = [ 500000, 500000 ]
    # print(vacSalary)
    
    # print('\nSalarios de los candidatos:')

    distances = []

    for candidate in candidates:
        if candidate['current_salary'] != '':
            canSalary = [ int(str(val.split(',')[0]) + str(val.split(',')[1])) for val in re.findall(r'(\d+\,\d+)', candidate['current_salary']) ]
        else:
            canSalary = [ 500000, 500000 ]
        
        if canSalary == []:
            canSalary = [ 500000, 500000 ]

        distance = 1

        if vacSalary[0] <= canSalary[0] <= vacSalary[1]:    # If in between salary range
            distance = (priority/2)
        elif canSalary[0] < vacSalary[0]:                   # If lower than salary range
            distance = priority
        else:                                               # If greater than salary range
            distance = 0

        distances.append({
            'id': candidate['id'],
            'dist': distance
        })
    
    # print()
    # print(distances)
    # print()

    for dist in distances:
        lastDist = None

        for resId, resDist in results.items():
            if resId == dist['id']:
                lastDist = resDist['dist']
            
        dist['dist'] += lastDist

    # print()
    # print(distances)
    # print()

    distances = order(distances)

    distancesNew = {}

    for dist in distances:
        distancesNew[dist['id']] = {
            'dist': dist['dist']
        }

    # print(distancesNew)

    return distancesNew

# We get the skills for each candidate and according to the level
# we put the priority of main and extra skills values
def orderBySkill(vacancy, candidates, results, priorities):
    print('\033[01m\033[35m--Entré a compareModules orderBySkill()--\033[0m\n')

    file = open('skills.data', 'rb')
    skills = pickle.load(file)

    vacancySkill = getSkill(vacancy['skill_name'], skills)
    # print(vacancySkill)

    skillLevels = {
        'Aprendiz': (1/4) * priorities[0],
        'Profesional': (2/4) * priorities[0],
        'Senior': (3/4) * priorities[0],
        'Experto': priorities[0]
    }

    extraSkillLevels = {
        'Aprendiz': (1/4) * priorities[1],
        'Profesional': (2/4) * priorities[1],
        'Senior': (3/4) * priorities[1],
        'Experto': priorities[1]
    }

    # print()
    # print('skillLevels: ')
    # print(skillLevels)
    # print()
    # print('extraSkillLevels: ')
    # print(extraSkillLevels)

    distances = []

    for candidate in candidates:
        # print('\nCandidate: {}'.format(candidate['id']))

        skillValue = 0

        for candSkill in candidate['skills']:
            skill = getSkill(candSkill['name'], skills)
            if skill['name'] == vacancySkill['name']:
                # print('Tiene:', skill['name'])
                skillValue += skillLevels[candSkill['level']]
            elif skill['field_id'] == vacancySkill['field_id']:
                # print('Extra:', skill['name'])
                skillValue += extraSkillLevels[candSkill['level']]
        
        # print(skillValue)

        distances.append({
            'id': candidate['id'],
            'dist': skillValue
        })

    # print()
    # print(distances)
    # print()

    for dist in distances:
        lastDist = None

        for resId, resDist in results.items():
            if resId == dist['id']:
                lastDist = resDist['dist']
            
        dist['dist'] += lastDist

    distances = order(distances)

    distancesNew = {}

    for dist in distances:
        distancesNew[dist['id']] = {
            'dist': dist['dist']
        }

    return distancesNew

# 1° Part: We get the job name, the description por each experience of the candidate
#          then we find out which of them talk about an skill of the vacancy
#          (with different priorities for last and current jobs and for the main and extras skills)
#
# 2° Part: We get the job name and compare the distance between it with the
#          vacancy job name, if it's bigger than the "type-job-percentaje" we add it to the
#          counter. Considereing the priority of this area and the different priorities for last and current jobs
def orderByJobs(vacancy, candidates, results, priorities):
    print('\033[01m\033[35m--Entré a compareModules orderByJobs()--\033[0m\n')

    file = open('skills.data', 'rb')
    skills = pickle.load(file)

    vacancySkill = getSkill(vacancy['skill_name'], skills)
    extraSkills = getExtraSkills(vacancySkill, skills)
    # print(extraSkills)

    distances = []
    distancesJobNames = []
    maxTotalDays = 0

    for candidate in candidates:

        totalJobPoints = 0
        totalDays = 0                   # Total days considering the priorities
        totalDaysNP = 0                 # Total days without considering the priorities
        totalJobSim = 0                 # Similarity between job names

        # print('\nCandidate: {}'.format(candidate['id']))
        for experience in candidate['experiences']:

            jobPoints = 0

            if experience['current_job'] == 1:                  # Current job
                if priorities[1] != 0:
                    pass
                else:
                    continue
            else:                                               # Not current job
                if priorities[0] != 0:
                    pass
                else:
                    continue

            # print('{} -> {}'.format(experience['place'], experience['job'] + experience['description']))
            for extraSkill in extraSkills:
                regex = re.compile('\W' + re.escape(extraSkill['name']) + '\W', re.IGNORECASE)

                # We get the matches in job and description for each experience
                found = re.findall(regex, experience['job'] + experience['description'])

                # print('{} -> {}'.format(extraSkill['name'], found))
                if found != []:

                    fact = 1
                    if experience['current_job'] == 1:                  # Current job
                        fact = priorities[1]
                    else:                                               # Not current job
                        fact = priorities[0]

                    # print(extraSkill['name'], ':::', vacancy['skill_name'])
                    if extraSkill['name'] == vacancy['skill_name']:
                        # print('Same')
                        jobPoints = fact
                    else:
                        if jobPoints < (fact / 4):
                            jobPoints = (fact / 4)
                    # print('{}'.format(jobPoints))
                    # print('{} -> {}'.format(extraSkill['name'], found))

            if experience['current_job'] == 0:
                time = experience['end_at']
                if time == '':
                    time = experience['start_at']
            else:
                time = datetime.now().strftime('%Y-%m-%d')
            
            if experience['start_at'] == '':
                time = days_between(datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'))
            else:
                time = days_between(experience['start_at'], time)


            # Compare string of jobs
            # print(vacancy['job'], '::::', experience['job'])
            typeDistance = similar(vacancy['job'], experience['job'])
            # print(typeDistance)
            if typeDistance > priorities[3]:
                totalJobSim += typeDistance * priorities[2]               # Distance between jobs
                if experience['current_job'] == 1:                  # Current job
                    totalJobSim *= priorities[1]
                else:                                               # Not current job
                    totalJobSim *= priorities[0]

                
            # print(totalJobSim)

            if jobPoints > 0:

                totalDaysNP += time

                if experience['current_job'] == 1:                  # Current job
                    totalDays += (time * priorities[1] * jobPoints)
                else:                                               # Not current job
                    totalDays += (time * priorities[0] * jobPoints)

                totalJobPoints += 1

            # print('Got {} in experience in {}'.format(jobPoints, totalDays))

        if totalDaysNP > maxTotalDays:
            maxTotalDays = totalDaysNP    

        # print('Candidate: {} -> {}pts in {}\n'.format(candidate['id'], totalJobPoints, totalDays))
        distances.append({
            'id': candidate['id'],
            'dist': totalDays
        })

        distancesJobNames.append({
            'id': candidate['id'],
            'dist': totalJobSim
        })

        # print()

    # print()
    # print(distances)
    # print()

    # print('Max: {}'.format(maxTotalDays))

    if maxTotalDays > 0:
        distances = [ { 'id': dist['id'], 'dist': (dist['dist'] / maxTotalDays) + getSameId(dist['id'], distancesJobNames)['dist']  } for dist in distances ]

    # print()
    # print(distances)
    # print()

    for dist in distances:
        lastDist = None

        for resId, resDist in results.items():
            if resId == dist['id']:
                lastDist = resDist['dist']
            
        dist['dist'] += lastDist

    distances = order(distances)

    distancesNew = {}

    for dist in distances:
        distancesNew[dist['id']] = {
            'dist': dist['dist']
        }

    # print()
    # print(distancesNew)
    # print()

    return distancesNew



# Some methods that we use

def order(distances):
    return sorted(distances, key = lambda i: i['dist'], reverse=True)

def getSkill(name, skills):
    for skill in skills:
        if skill['name'] == name:
            return skill
    return None

def getExtraSkills(vacSkill, skills):
    result = []
    for skill in skills:
        if skill['field_id'] == vacSkill['field_id']:
            result.append(skill)
    return result

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getSameId(dictId, list1):
    for item in list1:
        if str(item['id']) == str(dictId):
            return item
    return None