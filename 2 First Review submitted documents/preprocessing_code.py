#Preprocessing code

import pandas as pd
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_excel ('firstReview_Andhra_kyrnool.xlsx')
csv_lenth = len(df)
print(csv_lenth)

#Stop word Removal code

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_word = set(stopwords.words("english"))

new_lst = []
for x in range(csv_lenth):
  kf = (df.loc[x]['KccAns'])
  kf = kf.lower()
  words = word_tokenize(kf)
  filtered_sentence = [w.upper()  for w in words if not w in stop_word]
  new_lst.append(filtered_sentence)

df["stop removal"] = new_lst

#Spell checking code

from collections import Counter
def words(text): return re.findall(r'\w+', text.lower())
WORDS = Counter(words(open('big.txt').read()))
def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N
def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)
def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)
def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)
def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

new_lst2 = []
new_lst3 =[]
for x in range(csv_lenth):
  kf = (df.loc[x]['stop removal'])
  listlen  = len(kf)
  for y in range(listlen):
    corrected = correction(kf[y])
    new_lst3.append(corrected)
  new_lst2.append(new_lst3)
  new_lst3 =[]

df["Spell Correct"] = new_lst2

#Word Stemming code

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
new_lst2 = []
new_lst3 =[]
for x in range(csv_lenth):
  kf = (df.loc[x]['Spell Correct'])
  listlen  = len(kf)
  for y in range(listlen):
    steming = ps.stem(kf[y])
    new_lst3.append(steming)
  new_lst2.append(new_lst3)
  new_lst3 =[]

df["Stemmed"] = new_lst2

