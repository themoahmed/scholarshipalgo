
import pandas as pd
import csv

def collect_student_info():
    student_info = {}

    print("Please input your information")
    student_info['gpa'] = float(input("GPA (X.XX): "))
    student_info['act-score'] = int(input("ACT Score (Enter 0 if not taken): "))
    student_info['sat-scare'] = int(input("SAT score (Enter 0 if not taken): "))
    student_info['ethnicity'] = int(input("Ethnicty: 1.White 2.Black 3.Asian 4.Hispanic 5.Native-American 6.Other Please enter a number: "))
    student_info['study'] = int(input("Ethnicty: 1.ENGR 2.LAW 3.MED 4.BUAD 5.NURSE Please enter a number: "))
    student_info['State'] = input("Please enter your state postal code: ").upper()
    student_info['school'] = input('Please enter your university: ').lower()
    student_info['first-gen'] = input('Are you first generation (Y/N): ').upper()

    return student_info


momo = collect_student_info()
# for value in momo.values():
#     print(value)


df = pd.read_csv('scholarships.csv')


#when using function expects students_info['act-score']
#sorts dataframe by ACT
act = df.sort_values(by=['ACT']).reset_index(drop = True)

#uses act dataframe
def ACTbinary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = act.iloc[mid]['ACT']


        if mid_val <= target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low

#uses ACTbinary_search
def ACT_sorter(score):

    #act = sorted(df['ACT'].tolist())  # Sort the list of ACT scores
    

    scholarships = []

    index = ACTbinary_search(act.index, score)

    for i in range(index):
        scholarships.append(df.iloc[i])

    df2 = pd.concat(scholarships, axis=1).T

    return df2

        
qualify = ACT_sorter(momo['act-score'])
#print(momo['act-score'])
#print(qualify)



















