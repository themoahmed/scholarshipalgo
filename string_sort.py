from bisect import bisect_left


def binary_serch_ethnicity(sorted_ethnicites, target_ethnicity):
    index = bisect_left(sorted_ethnicites, target_ethnicity)
    return index if index != len(sorted_ethnicites) and sorted_ethnicites[index] == target_ethnicity else -1


sorted_ethnicites = data['Ethnicity'].tolist()
# user input for ethnicity
user_input = int(input("Enter 1 for black 2 for Hispanic and 3 for aisan"))
maping = {1: 'Black', 2: 'Hispanic', 3: 'Aisan'}
target_ethnicity = maping.get(user_input)

if target_ethnicity is not None:
    index = binary_serch_ethnicity(sorted_ethnicites,target_ethnicity)
    if index == -1:
        print(f"ethnicity '{target_ethnicity}' not found")
    else:print(f"ethnicity  '{target_ethnicity}' found at index {index} ")


    # filter scholorships based on ethnicity
    qualifed_scholarships = data[data['Ethnicity']] == target_ethnicity
    print("qualified schlorships based on ehtnicity")
    print(qualifed_scholarships)
else:
        print("invalid input for ehtniciity")

