import requests
import json


#result = requests.get('https://api.github.com/repos/zorro1992/askdevops',headers={'Authorization':'token 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'})

number_of_results = 1

result = requests.get('https://randomuser.me/api/?exc=login&results='+ str(number_of_results))

#print(result)

repos = json.loads(result.content.decode('utf-8'))


# print(type(repos))
# print(repos)

# for x in repos.values():
#     print(x)
#     print(type(x))

for x in range(0,number_of_results):
    print(repos['results'])

