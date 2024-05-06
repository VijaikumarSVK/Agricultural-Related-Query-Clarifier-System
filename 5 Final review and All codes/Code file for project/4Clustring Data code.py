import os, glob
import pandas as pd
import numpy as np
import csv


total_dictionary = {}

with open('/content/drive/MyDrive/project/Data Set/Final_merged1.csv') as fin:
    reader = csv.DictReader(fin)
    
    for row in reader:
      values = [row['QueryType'], row['StateName'],row['DistrictName'],row['CreatedOn'],row['Answer']]

      query = row['Query']
      query = (" ".join(query.split()))
        # branches[row['River Name']].append(branch)
      total_dictionary.setdefault(query, [])
      total_dictionary[query].append(values)

with open('/content/drive/MyDrive/project/Data Set/Final_merged2.csv') as fin:
    reader = csv.DictReader(fin)
    
    for row in reader:
      values = [row['QueryType'], row['StateName'],row['DistrictName'],row['CreatedOn'],row['Answer']]

      query = row['Query']
      query = (" ".join(query.split()))
        # branches[row['River Name']].append(branch)
      total_dictionary.setdefault(query, [])
      total_dictionary[query].append(values)

with open('/content/drive/MyDrive/project/Data Set/Final_merged3.csv') as fin:
    reader = csv.DictReader(fin)
    
    for row in reader:
      values = [row['QueryType'], row['StateName'],row['DistrictName'],row['CreatedOn'],row['Answer']]

      query = row['Query']
      query = (" ".join(query.split()))
        # branches[row['River Name']].append(branch)
      total_dictionary.setdefault(query, [])
      total_dictionary[query].append(values)
