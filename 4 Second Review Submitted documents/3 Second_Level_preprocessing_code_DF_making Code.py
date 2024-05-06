#Merging all year wise DataSet Collected from KCC 

import os, glob
import pandas as pd
import numpy as np
import csv

path = "/content/drive/MyDrive/project/Data Set/Preprocessed files/"

all_files = glob.glob(os.path.join(path, "201*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged   = pd.concat(df_from_each_file, ignore_index=True)
print(len(df_merged))


df_merged.to_csv( "merged.csv")


# The merged fill having total of 27,98,002 data for that we need to seperated those in different csv

df1 = df_merged.head(1048000)
df2 = df_merged.loc[1048001:2050001]
df3 = df_merged.loc[2050002:]

df1.to_csv( "merged1.csv")
df2.to_csv( "merged2.csv")
df3.to_csv( "merged3.csv")


# After seperating still some preprocessing step to follow
# like removing unwanted column and deleting unwanted special character

df = pd.read_csv('/content/merged3.csv')
print(len(df))

df = df.drop(['Season','Sector','Category','Crop','QueryText','KccAns','BlockName',df.columns[0]], axis = 1)

dictionary = {'\?':'', '\@':'','!':'','#':'','-':'',',':'','>':'','<':'','\/':'','\(':'','\)':'','\|':'','\–':'','\\t':'','\*':'','\=':'','\;':''}
df.replace(dictionary, regex=True, inplace=True)

df = df.replace(r'^\s*$', np.NaN, regex=True)


#In this we are eliminating all the null Cell form the csv file and make them ascending order


df = df[df[['Final Query Correct', 'Final Anwer Correct']].notnull().all(1)]

df.sort_values(["Final Query Correct"], 
                    axis=0,
                    ascending=[True], 
                    inplace=True)

df.reset_index(drop=True, inplace=True)

first_column = df.pop('Final Query Correct')

df.insert(0, 'Query', first_column)

df.rename(columns={"Final Anwer Correct": "Answer"}, inplace=True)

#By this we are creating new csv file

df.to_csv( "Final_Processed.csv")

print(len(df))
print(df.Query.nunique())
print(df.Answer.nunique())

