import json
import sys

for arg in sys.argv[1:]:
    with open(arg, 'r', encoding='utf-8') as myfile:
        data = myfile.read()

# with open('test.json', 'r', encoding='utf-8') as myfile:
#    data = myfile.read()

inputJson = json.loads(data)

print (inputJson["fightName"])  

playerList = []

for user in inputJson["players"]:
    player = user["name"]
    prof = user["profession"]
    for targets in user["dpsTargets"][0]:
        dps = targets["dps"]
        break
    player = dict({'Player': player, 'Profession': prof, 'DPS': dps})
    playerList.append(player)

playerList.sort(reverse = True, key=lambda a: a['DPS'])
output = dict({'Data': playerList})

jsonString = json.dumps(output)
print(jsonString)
with open ('output.json', 'w', encoding='utf-8') as outfile:
    outfile.write(jsonString)