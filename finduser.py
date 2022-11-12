import csv

users = []
count = 0
with open('user_sorted.csv', 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        if lines == []:
            pass
        else:
            if count == 0:
                count += 1
                pass
            else:
                users.append(lines)


# try:
#     print(0)
# except print(0):
#     pass
userdata = []
id = input("Enter id of user: ")
for user_data in users:
    if user_data[0] == id:
        userdata = user_data
        break
    else:
        userdata = 'Not Found'

print(userdata)
