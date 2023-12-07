import pandas as pd
import csv

data = pd.read_csv(r"C:\Users\nkban\PycharmProjects\pythonProject4\scholarships.csv")
data.sort_values(by='Study', inplace=True)

area_of_study_mapping = {
    '1': 'ENGR',
    '2': 'Law',
    '3': 'MED',
    '4': 'BUAD',
    '5': 'NURSE'

}

def binary_serch(data,target):
    left, right = 0,  len(data) -1
    matches = []

    while left <= right:
        mid = (left + right) // 2
        mid_value = str(data.iloc[mid]['Study'])
        #print(mid_value)
        #print(target)
        if mid_value == str(target):
            matches.append(data.iloc[mid]['Scholarship Name'])
            left_match, right_match = mid -1, mid +1
           # print("hello")
            while left_match >= 0 and str(data.iloc[left_match]['Study']) == target:
                matches.append(data.iloc[left_match]['Scholarship Name'])
                left_match -=1
            while right_match < len(data) and str(data.iloc[right_match]['Study']):
                matches.append(data.iloc[right_match]['Scholarship Name'])
                right_match += 1
            #print(matches)
            return matches

            #return mid
        elif mid_value < str(target):
            left = mid+1
        else:
            right = mid -1

    #returns -1 if not found
    return matches

user_input_code = input('Enter the area of study  (1 for engernering 2 for law 3 for med and 4 for buinises and 5 for nurse) :')
user_input = area_of_study_mapping.get(user_input_code)
if user_input is None:
    print(f"invalid user input")
else:
    matches = binary_serch(data, user_input)

    if matches:
        print(f"qualified scholorships for area of study '{user_input}':")
        for scholarship in matches:
            print(scholarship)
    else:
        print("No scholarships found for this study area")
        #print(data)