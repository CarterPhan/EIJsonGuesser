import json
import sys

# Green: Right Elite, Right Place
# Yellow: Right Elite, Wrong Place
# Orange: Right Profession, Wrong Elite (No Hint on Place)
# Red: This profession/elite is not found
# First work with Professions, then Elites

# for arg in sys.argv[1:]:
#     with open(arg, 'r', encoding='utf-8') as myfile:
#         data = myfile.read()

with open('output.json', 'r', encoding='utf-8') as myfile:
    data = myfile.read()
        
inputJson = json.loads(data)

tempProfessionList = ['Necromancer', 'Mesmer', 'Elementalist', 'Engineer', 'Thief', 'Ranger', 'Warrior', 'Guardian', 'Revenant']
necroList = ['Reaper', 'Scourge', 'Harbinger']
mesmerList = ['Chronomancer', 'Mirage', 'Virtuoso']
eleList = ['Tempest', 'Weaver', 'Catalyst']
engiList = ['Scrapper', 'Holosmith', 'Mechanist']
thiefList = ['Daredevil', 'Deadeye', 'Spectre']
rangerList = ['Druid', 'Soulbeast', 'Untamed']
warrList = ['Berserker', 'Spellbreaker', 'Bladesworn']
guardList = ['Dragonhunter', 'Firebrand', 'Willbender']
revList = ['Herald', 'Renegade', 'Vindicator']
listofLists = [necroList, mesmerList, eleList, engiList, thiefList, rangerList, warrList, guardList, revList]
professionList = []
for i, j in zip(tempProfessionList, listofLists):
    tempDict = dict({'Profession': i, 'Elites': j})
    professionList.append(tempDict)

playerList = []

for user in inputJson["Data"]:
    prof = user["Profession"]
    dps = user["DPS"]
    player = user["Player"]
    jsonInput = dict({'p': prof, 'd': dps, 'l': player})
    playerList.append(jsonInput)

numbersList = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth']
userInput = []

for i in numbersList:
    flag = 'red'
    str = 'Input your guess for ' + i + ': '
    guess = input(str)
    userInputTemp = dict({'Number': i, "Guess": guess, 'Flag': flag})
    userInput.append(userInputTemp)

for i, j in zip(userInput, playerList):
    if i['Guess'] == j['p']:
        print ('True')
    else:
        print ('False')