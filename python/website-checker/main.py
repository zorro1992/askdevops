#import csv

import requests
import csv

status_dict = {"Website": "Status"}

website = "https://www.youtube.com/"
status = requests.get(website).status_code
print(status)

if status == 200:
    status_dict[website] = "working"
else:
    status_dict[website] = "not working"


print(status_dict)


with open("website_status.csv", "w", newline="") as file:
    csv_writers = csv.writer(file)
    for key in status_dict.keys():
        csv_writers.writerow([key, status_dict[key]])
        
        