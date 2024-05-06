# Data Frame Creation based on Unique Query and Model Training and getting the required response

## Importing libraries
"""

import os, glob
import pandas as pd
import numpy as np
import csv
import pickle
import sklearn
import urllib.request
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# sample_df = pd.read_csv('/content/drive/MyDrive/project/Data Set/Final_merged1.csv')

"""### Data Frame is stored in the form of Dictionay based on unique query"""

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

len(total_dictionary)

# keys_list = list(total_dictionary)
# k = keys_list[150]
# l = (total_dictionary[k])

# l = (total_dictionary[k])
# print(len(l))
# for i in l:
#   # print(i[0],i[1],i[2],i[3],i[4])
#   print(i[4])

# keys_list = list(total_dictionary)

# for i in range(2000):
#   k = keys_list[i]
#   print(k)

"""## Creating an Empty list and append the unique(query value)"""

lis = []
for key in total_dictionary.keys():
  # print(key)
  lis.append(key)

"""# **Model Training Section**

The sentence-transformers allows to train and use Transformer models for generating sentence and text embeddings .
"""

!pip install -U sentence-transformers

model_name = 'bert-base-nli-mean-tokens'

from sentence_transformers import SentenceTransformer

"""Initializing the model"""

model = SentenceTransformer(model_name)

"""## gives a list of sentence to train in the model"""

# sentence_vecs = model.encode(lis)

# sentence_vecs[165954]

# save the model to disk
# filename = 'finalized_model.sav'
# pickle.dump(sentence_vecs, open(filename, 'wb'))

"""## Loading the trainined Model from Drive"""

# load the model from disk

filename = '/content/drive/MyDrive/project/Data Set/finalized_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))

# loaded_model.shape
# loaded_model[56934]

from sklearn import metrics
from sklearn.metrics.pairwise import cosine_similarity

"""Getting sample query randomly"""

# print(lis[200000:200005])

"""Manually Giving Query for testing"""

input_Sen = "Banana tree yellow leaves issue was happing frequently"

"""# Preprocessing the Input Text

## Stop word Removal
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_word = set(stopwords.words("english"))

UserQuery = list(input_Sen.split(" "))

UserQuery = " ".join(str(x) for x in UserQuery)
UserQuery = UserQuery.lower()

UserQuerys = word_tokenize(UserQuery)

filtered_sentenceQuery = [w.upper()  for w in UserQuerys if not w in stop_word]

filtered_sentenceQuery = " ".join(str(x) for x in filtered_sentenceQuery)

input_Sen_stop_word = filtered_sentenceQuery

# print(input_Sen_stop_word)

"""## Language Translation"""

!pip install googletrans==3.1.0a0

from googletrans import Translator
translator = Translator()

input_Sen_translated = translator.translate(input_Sen_stop_word, dest='en').text

# input_Sen_translated

"""## Word Stemming"""

from nltk.stem import PorterStemmer

ps = PorterStemmer()

new_lst = []
Query = (input_Sen_translated)
Query = str(Query)
Query = list(Query.split(" "))

listlen1  = len(Query)

for y in range(listlen1):
    steming = ps.stem(Query[y]).upper()
    new_lst.append(steming)
  
listToStr = ' '.join([str(elem) for elem in new_lst])

input_Sen = listToStr

print(input_Sen)

"""Converting the Query Sentence to vector"""

input_Sen = model.encode(input_Sen)

input_Sen

similarity = cosine_similarity(
    [input_Sen], loaded_model[1:]
)

maximum = max(similarity)
maxi = max(maximum)
print(maxi)
index_of_maximum = np.where(maxi == maximum)

Query_index = index_of_maximum[0][0]+1
print(Query_index)

print(lis[Query_index])
key = lis[Query_index]

l = (total_dictionary[key])
ans_list = []
print("Number of Response from the particular Query:",len(l))
for i in l:
  # print(i[0],i[1],i[2],i[3],i[4])
  ans_list.append(i[4])
  # print(i[4])

"""Translating the list of answer to enlish language """

ans_list_new = []
for ans in ans_list:
  val = translator.translate(ans, dest='en').text
  ans_list_new.append(val)

# ans_list_new

"""## Lesk Algorithm implementation

Converting list of answer to *dictionary*
"""

from nltk.tokenize import word_tokenize

d = {}
for index, value in enumerate(ans_list_new):
    d[index+1] = value

def by_value(item):
    return item[1]

def lesk(sentence , dict_s ):
    y = {}
    z = 0
    sentence = word_tokenize(sentence)
    for key, value in dict_s.items():
        x = 0
        k = word_tokenize(value)
        
        for i in range(len(k)):            
          for j in range(len(sentence)):
              if sentence[j] == k[i]:
                 x += 1
                    
        y[key] = x
        
    for k, v in sorted(y.items(), key=by_value):
        z = k    
        
    return dict_s[z]

"""Final Predicted answer from the given query"""

answer = lesk(key , d )
print("Answer for given Query:",answer)