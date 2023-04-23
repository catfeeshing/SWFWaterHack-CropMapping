import pandas as pd
import os

path = '.'
out_file = 'combined_data.csv'

# get list of csv files in path
file_list = [f for f in os.listdir(path) if f.endswith('.csv')]

# read first file to get header
df = pd.read_csv(os.path.join(path, file_list[0]))
df.to_csv(out_file,mode='a',index=False)
header = list(df.columns)
print(header)
# append the rest of the files to the end of the first file
for i in range(1, len(file_list)):
    file_path = os.path.join(path, file_list[i])
    df = pd.read_csv(file_path)
    df.to_csv(out_file, mode='a', index=False, header=False)

# read final output file and print the shape
df_final = pd.read_csv(out_file)
print(df_final.shape)
