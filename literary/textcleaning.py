# librarys for frame, lower() function
# !pip install pandas
import pandas as pd
import re

# convert text in frame
with open('../docsources/text1.txt', 'r') as file:
    #dataframe = pd.DataFrame(file) (same effect, but to low parameters)
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    dataframe =pd.read_csv(file, encoding='utf-8',delimiter="-", engine="python")
    print(dataframe)
    string_dataframe = str(dataframe)
    lower_dataframe = string_dataframe.lower()
    print("lower_dataframe: " + lower_dataframe)
    # https://docs.python.org/3/library/re.html
    #dataframe = dataframe.str.replace('[^\w\s]', "")
    #print("dataframe_cleaned: " + dataframe)


with open('../docsources/text.txt', 'w+') as file:
    # dataframe wird nicht in file geschrieben:
    file.write("Dataframe as string:" + string_dataframe)
    file.write("Dataframe as string in lowercase:" + lower_dataframe)
    #file.write("Dataframe as string in lowercase cleaned:" + dataframe)




