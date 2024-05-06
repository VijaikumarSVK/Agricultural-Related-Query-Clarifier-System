import urllib.request
import json
import os
import csv

from googletrans import Translator 
translator = Translator()
dist = 1
state = 1
month = 1
year = 2020
dataset = 1
count = 0
while (2022 >= year):
    if(len(str(state))==1):
        states = '0'+str(state)
    else:
        states = str(state)

    if(len(str(dist))==1):
        distct = '0'+str(dist)
    else:
        distct = str(dist)

    if(len(str(month))==1):
        months = '0'+str(month)
    else:
        months = str(month)

    years = str(year)

    request = urllib.request.urlopen("http://dackkms.gov.in/Account/API/kKMS_QueryData.aspx?StateCD="+states+"&DistrictCd="+states+distct+"&Month="+months+"&Year="+years)    
    for i in request:
        print(len(i))
        if len(i)<100:
            state += 1
            dist = 0
            dataset -=1
        if(state==39):
            month +=1
            state = 1
            dist = 0
        if(month==12):
            year += 1
            state = 1
            month = 1
            dist = 0
            count = 0
            continue
        try:
            request1 = urllib.request.urlopen("http://dackkms.gov.in/Account/API/kKMS_QueryData.aspx?StateCD="+states+"&DistrictCd="+states+distct+"&Month="+months+"&Year="+years)
            data = json.load(request1)
            
            datas = data['data']
            #print(datas)
        except Exception:
            pass

    save_path = "F:/project details/vj/json/"
    filename = str(years)+str(states)+str(distct)
    
    file_name = str(year)
    
    completeName = os.path.join(save_path, file_name+".json")
    with open(completeName, "w",encoding="utf-8") as outfile:
        json.dump(datas, outfile)
    
    dist+=1


    with open("F:/project details/vj/json/"+file_name+".json") as json_file:
        jsondata = json.load(json_file)
        #print(jsondata)
 
    data_file = open("F:/project details/vj/csv/"+file_name+".csv", 'a', newline='',encoding='utf-8')
    csv_writer = csv.writer(data_file)
    #next(csv_writer)
 
    
    for xyz in jsondata:
        #print(xyz)
        if count == 0:
            header = xyz.keys()
            csv_writer.writerow(header)
            #print(header)
            count = 1

        #print("*********Before Translations********")
        #print(xyz.values())
        
        trans_val = xyz['KccAns']

        try:
            translate_text = ((translator.translate(trans_val, dest='en')).text)  
            xyz['KccAns'] = translate_text
        except:
            pass
        #print("#########After Translations##########")
        #print(xyz.values())
        csv_writer.writerow(xyz.values())

    data_file.close()
    
    print("dist="+distct)
    print("states="+states)
    print("months="+months)
    print("year="+years)
    print("data set="+str(dataset))
    dataset +=1
    print("*************")



#pip install googletrans==3.1.0a0
