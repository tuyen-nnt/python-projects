import csv
import pandas as pd

df = pd.read_csv('~/Downloads/bao.csv')

df[['ward_id', 'district_id', 'region_id']] = df[['ward_id', 'district_id', 'region_id']].astype(int)

df.to_csv('bao-converted.csv', quoting=csv.QUOTE_NONNUMERIC)

print(df)

# https://stackoverflow.com/questions/15891038/change-column-type-in-pandas
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html