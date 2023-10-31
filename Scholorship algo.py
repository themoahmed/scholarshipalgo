import pandas as pandas
import pip
import pandas as pd



# geting data from csv file
data = pd.read_csv("scholorship.csv")
#sorting data based on scolorship score (decnding order)
data = data.sort_values(by= "scholorship score", asending = False)
# add sorted data to a new coloum  to the dataframe
data["sorted scores"] = range(1,len(data)+1)
#save dataframe to csv file
data.to.csv("scholarships.csv", index=False)
#print the sorted dataframe
print(data)


