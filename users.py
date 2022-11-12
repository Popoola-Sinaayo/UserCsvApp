import requests
import csv

response = requests.get(
    'https://random-data-api.com/api/v2/users', params={'size': 10})

data = response.json()

with open('users.csv', mode='w') as user_file:
    fieldnames = ['id', 'FirstName', 'LastName', 'Username',
                  'Email', 'Avatar', 'Gender', 'Dob', 'Address']
    writer = csv.DictWriter(user_file, fieldnames=fieldnames)
    writer.writeheader()
    for datas in data:
        writer.writerow({'id': datas['id'], 'FirstName': datas['first_name'], 'LastName': datas['last_name'], 'Username': datas['username'], 'Email': datas["email"],
                         'Avatar': datas["avatar"], 'Gender': datas["gender"], "Dob": datas["date_of_birth"],  "Address": f'{datas["address"]["city"]}'})

print('done')
