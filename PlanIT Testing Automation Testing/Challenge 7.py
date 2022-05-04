import pandas as pd
import sys

#terminal parameter:
csv_data = sys.argv[1]

df = pd.read_csv(csv_data, skipinitialspace=True, header=0)

print(df)
print("\n")

col_heading = input("Enter Column Heading: ")
value = input("Enter Lookup Value: ")

print(df.loc[df[col_heading] == value])