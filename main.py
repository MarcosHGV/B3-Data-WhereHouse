import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 2000)

file_path = 'caminho'
df = pd.read_csv(file_path, delimiter='\t')  # ou delimiter=' ' se for separado por espaço

print(df.head())