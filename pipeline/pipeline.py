import sys
import pandas as pd

##print("arguments", sys.argv)
month = int (sys.argv[1])
df = pd.DataFrame({"day": [1, 2], "num_pass": [3, 4]})
df['month']= month
print(df.head())

df.to_parquet(f"output_{month}.parquet")
day = int(sys.argv[1])
print(f"Running pipeline for day {day}")