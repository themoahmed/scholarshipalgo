import pandas as pd


def main():
    data = pd.read_csv(r"C:\Users\phurl\Downloads\scholarships (1).csv")
    df = pd.DataFrame(data)
    input = collect_student_info()
    if input['first-gen']=='N':
        df=df[df['First Gen'] != 'Y']
    df = stringSort(df, input['ethnicity'], 'Ethnicity')
    df = stringSort(df, input['study'], 'Study')
    df = stringSort(df, input['State'], 'State')
    df = stringSort(df, input['school'], 'School')
    df= numSort(df,input['gpa'],'GPA')
    df= numSort(df,input['sat-score'],'SAT')
    df= numSort(df,input['act-score'],'ACT')
    df["scholarship_score"] = round((df["Scholarship Award"] / df["Number applied"]), 2)
    sorted_df= df.sort_values(by="scholarship_score", ascending=False)
    print(sorted_df.head(3))

def collect_student_info():
    student_info = {}

    print("Please input your information")
    student_info['gpa'] = float(input("GPA (X.X): "))
    student_info['act-score'] = int(input("ACT Score (Enter 0 if not taken): "))
    student_info['sat-score'] = int(input("SAT score (Enter 0 if not taken): "))
    student_info['ethnicity'] = int(input("Ethnicty: 1.White 2.Black 3.Asian 4.Hispanic 5.Native-American 6.Other Please enter a number: "))
    student_info['study'] = int(input("Plan of Study: 1.ENGR 2.LAW 3.MED 4.BUAD 5.NURSE 6. Other Please enter a number: "))
    student_info['State'] = input("Please enter your state abbreviation: ").upper()
    student_info['school'] = input('Please enter your university: ').lower()
    student_info['first-gen'] = input('Are you first generation (Y/N): ').upper()
    return student_info


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def mergeSort(s_list, low, high):
    if ((high - low) < 50):
        insertionSort(s_list)
    else:
        if low < high:
            mid = low + (high-low) // 2
            mergeSort(s_list, low, mid)
            mergeSort(s_list, mid + 1, high)
            merge(s_list, low, mid, high)

def numSort(df, inputVal, var):
    if inputVal==0:
        return df
    arr = df.to_numpy()
    length = len(arr)
    list = [0 for y in range(length)]
    if(var=='GPA'):
        for x in range(0,length):
            list[x]=arr[x][4]
    if(var=='SAT'):
        for x in range(0,length):
            list[x]=arr[x][3]
    if(var=='ACT'):
        for x in range(0,length):
            list[x]=arr[x][2]
    mergeSort(list, 0, length-1)
    count=0
    y=0
    if inputVal>=list[length-1]:
        return df
    while(list[y]<=inputVal):
        count+=1
        y+=1
    df=df.sort_values(var)
    return df.iloc[:count]



def binary_search(data,low,high,target,var):
    data = data.sort_values(var)
    if high >= low:

        mid = (high + low) // 2
        mid_value = str(data[var].loc[data.index[mid]])
        if mid_value == target:
            left = mid
            right = mid
            while (str(data[var].loc[data.index[right]]) == target):
                right += 1
            while(str(data[var].loc[data.index[left]])==target):
                left-=1
            return data.iloc[left+1:right]
        elif str(data[var].loc[data.index[mid]]) > target:
            return binary_search(data, low, mid - 1, target, var)

        else:
            return binary_search(data, mid + 1, high, target, var)
    else:
        df = pd.DataFrame()
        return df

def find_na(data, var):
    length = len(data)
    data = data.sort_values(var)
    index=0
    while(str(data[var].loc[data.index[index]]) != 'nan'):
        index+=1
    df = data.iloc[index:length-1]
    return df

def stringSort(df, input, var):
    length=len(df)
    if var=='Ethnicity':
        if input==1:
            val='white'
        elif input==2:
            val='Black'
        elif input==3:
            val='Asian'
        elif input==4:
            val='Hispanic'
        elif input==5:
            val='American Indian'
        else:
            return find_na(df,var)
        dataBS=binary_search(df,0,length-1,val,var)
        data = find_na(df,var)
        data = pd.concat([data,dataBS], ignore_index=True)
        return data
    elif var=='Study':
        if input==1:
            val='ENGR'
        elif input==2:
            val='LAW'
        elif input==3:
            val='MED'
        elif input==4:
            val='BUAD'
        elif input==5:
            val='NURSE'
        else:
            return find_na(df, var)
        dataBS = binary_search(df, 0, length - 1, val, var)
        data = find_na(df, var)
        data = pd.concat([data,dataBS],ignore_index =True)
        return data
    elif var=='State':
        data = find_na(df, var)
        dataBS = binary_search(df,0,length-1,input,var)
        data = pd.concat([data, dataBS],ignore_index = True)
        return data
    elif var=='School':
        data= find_na(df, var)
        dataBS = binary_search(df,0,length-1,input,var)
        data = pd.concat([data, dataBS], ignore_index=True)
        return data
    else:
        return df

main()
