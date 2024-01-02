import pandas as pd

excelInput = 'C:/Users/liamn/IdeaProjects/CanisterListFilter/CanisterList_placeholder.xlsx'
df = pd.read_excel(excelInput)

searchColumn = 'CanisterName'

df['StrippedText'] = df[searchColumn].str.replace(r'(_1|_2|_3|_4)', '', regex=True)

unique_rows_df = df.drop_duplicates(subset='StrippedText', keep=False).copy()
unique_rows_df.drop(columns=['StrippedText'], inplace=True)

excelOutput = "C:/Users/liamn/IdeaProjects/CanisterListFilter/CanisterList_filtered.xlsx"
unique_rows_df.to_excel(excelOutput, index=False)

print(f"Duplicated rows removed from {excelInput}")
