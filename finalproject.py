#imports
import csv
import requests
import pandas as pd
from bokeh.charts import Bar, output_file, save

#open csv and create writer
file = open("level.csv","w")
csv = csv.writer(file,delimiter = ",")
csv.writerow(["id","lvl"])

#use for loop for 6 different pokemon evolution trees
for x in range (1,7):
    endpoint = "http://pokeapi.co/api/v2/"
    num = "evolution-chain/"+str(x)+"/"
    url = endpoint+num
    payload = {}
    r = requests.get(url, params=payload)
    print(r)
    d = r.json()
    lvl = d["chain"]["evolves_to"][0]["evolution_details"][0]["min_level"]
    csv.writerow([x, lvl])
file.close()

#let bokeh read csv file
data = pd.read_csv("level.csv")
#make bar graph
bar = Bar(data, values="lvl", label="id", title="Pokemon Evolution Level Comparison")
output_file("bar.html")
#make file
save(bar)

    

