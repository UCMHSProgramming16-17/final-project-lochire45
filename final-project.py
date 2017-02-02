import csv
import requests

# acquire pokemon id
identity = input("What is your pokemon's ID number?")
url= "https://pokeapi.co/api/v2/evolution-chain/" + identity

# get request
p = requests.get(url)
poke = p.json()
print(poke)

# write to csv file
variable = open('pokemon.csv', 'w', newline = '')
writer = csv.writer('variable', delimiter=',')
writer.writerow(['item1', 'item2', 'item3'])
