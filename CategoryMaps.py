import pandas as pd
edu_map = {
    "1st-4th" : "Pre-HS", "5th-6th" : "Pre-HS", "Preschool" : "Pre-HS", "7th-8th" : "Pre-HS",
    "9th" :  "Some-HS", "10th" :  "Some-HS", "11th" :  "Some-HS", "12th" :  "Some-HS",
    "Some-college" :  "College", "Assoc-voc" :  "College", "Assoc-acdm" :  "College",
    "Masters" : "Advanced", "Doctorate" : "Advanced", "Prof-school" : "Advanced"
}

def groupHours(data):
    data.loc[data["hours-per-week"] <= 10, "hwpw"] = "0-10"
    data.loc[(data["hours-per-week"] > 10) & (data["hours-per-week"] <= 25), "hwpw"] = "11-25"
    data.loc[(data["hours-per-week"] > 25) & (data["hours-per-week"] <= 39), "hwpw"] = "26-39"
    data.loc[(data["hours-per-week"] == 40), "hwpw"] = "40"
    data.loc[(data["hours-per-week"] > 40) & (data["hours-per-week"] <= 60), "hwpw"] = "41-60"
    data.loc[(data["hours-per-week"] > 60), "hwpw"] = "60+"

def groupAge(data):
    bins = [17, 25, 35, 50, 65, 100]
    labels = ["Early Career", "Establishing", "Peak", "Late Career", "Retirement"]
    data["age-group"] = pd.cut(data["age"], bins=bins, labels=labels, right=False)

def dropColumns(data):
    data.drop(columns = ["native-country",
                         "hours-per-week",
                         "fnlwgt",
                         "education-num",
                         "age"
                         ], inplace=True)