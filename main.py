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


# momo = collect_student_info()
# for value in momo.values():
#     print(value)

df = pd.read_csv('scholarships.csv')
print(df)

# Access specific columns and turn them into lists
# names = df['Name'].tolist()
# ages = df['Age'].tolist()




