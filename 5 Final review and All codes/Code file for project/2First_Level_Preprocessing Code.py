#Importing Libraries and CSV file we need

import pandas as pd
import nltk
import re
import csv
nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_csv ('2019.csv')
csv_lenth = len(df)
print(csv_lenth)


#Word Stemming Code 


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
new_lst2 =[]
new_lst3 =[]
new_lst4 =[]
new_lst5 =[]
for x in range(csv_lenth):

  Query = (df.loc[x]['QueryText'])
  Query = str(Query)
  Query = list(Query.split(" "))
  
  Ans = (df.loc[x]['KccAns'])
  Ans = str(Ans)
  Ans = list(Ans.split(" "))

  listlen1  = len(Query)
  listlen2  = len(Ans)
  for y in range(listlen1):
    steming = ps.stem(Query[y]).upper()
    new_lst3.append(steming)

  for y in range(listlen2):
    steming = ps.stem(Ans[y]).upper()
    new_lst5.append(steming)

  new_lst2.append(new_lst3)
  new_lst4.append(new_lst5)
  new_lst3 =[]
  new_lst5 =[]

df["Query Stemming"] = new_lst2
df["Answer Stemming"] = new_lst4


#Stop Word Removal Code

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_word = set(stopwords.words("english"))

new_lst_ans = []
new_lst_query = []
for x in range(csv_lenth):
  UserQuery = (df.loc[x]['Query Stemming'])
  KccAnswers = (df.loc[x]['Answer Stemming'])

  UserQuery = " ".join(str(x) for x in UserQuery)
  KccAnswers = " ".join(str(x) for x in KccAnswers)
  
  UserQuery = UserQuery.lower()
  KccAnswers = KccAnswers.lower()

  UserQuerys = word_tokenize(UserQuery)
  KccAns = word_tokenize(KccAnswers)

  filtered_sentenceQuery = [w.upper()  for w in UserQuerys if not w in stop_word]
  filtered_sentenceAnswer = [w.upper()  for w in KccAns if not w in stop_word]

  filtered_sentenceQuery = " ".join(str(x) for x in filtered_sentenceQuery)
  filtered_sentenceAnswer = " ".join(str(x) for x in filtered_sentenceAnswer)

  new_lst_query.append(filtered_sentenceQuery)
  new_lst_ans.append(filtered_sentenceAnswer)

df["Final Query Correct"] = new_lst_query
df["Final Anwer Correct"] = new_lst_ans

del df['Query Stemming']
del df['Answer Stemming']


#Creating First level preprocessing CSV file
df.to_csv(r'/content/2019_preprocessed.csv', index = False)