from CategoryMaps import *

df = pd.read_csv("adult_income.csv")
df.fillna("Unknown", inplace=True)
df.replace("?", "Unknown", inplace=True)
df.replace("<=50K.", "<=50K", inplace=True)
df.replace(">50K.", ">50K", inplace=True)


# Separate the df into groups using pandas for input into f_oneway
#group1 = df[df['group'] == 'A']['value']
#group2 = df[df['group'] == 'B']['value']
#group3 = df[df['group'] == 'C']['value']

df["education"] = df["education"].replace(edu_map)

groupHours(df)
groupAge(df)
dropColumns(df)

df.info()
print(df["income"].unique())