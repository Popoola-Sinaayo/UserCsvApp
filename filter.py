import csv


araay = []
title = []
with open('users.csv', mode='r')as file:

    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    count = 0
    print(csvFile)
    # for lines in csvFile:
    #     if lines == []:
    #         pass
    #     else:
    #         if count == 0:
    #             araay.append(lines)
    #             count +=1
    #         else:
    #             for i in range(len(araay)):
    #                 if lines[3][0] < araay[i][3][0]:
    #                     # araay.clear()

    for lines in csvFile:
        if lines == []:
            pass
        else:
            if count == 0:
                count += 1
                title = lines
                pass
            else:
                araay.append(lines)





def extract_letter(data):
    return data[3][0]


araay.sort(key=extract_letter)


with open('user_sorted.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(title)

    # writing the data rows
    for data in araay:
        print(data)
        csvwriter.writerow(data)
print('done')
