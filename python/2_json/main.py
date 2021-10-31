import json
import plotly.io as pio

with open('data.json') as data_file:
    data = json.load(data_file)

#print(data)
# name=data[0]['name']
# print(name)

final={}
output=[]
for item in data:
    name=item['name']
    country=item['country']

    filter_data = {
        "name":name,
        "country": country
    }

    output.append(filter_data)

for x in output:
    print(x['name'], "is from", x['country'])

pio.show(output)