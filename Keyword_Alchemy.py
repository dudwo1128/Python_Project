import json
import requests
import csv
from os.path import join, dirname
import pandas as pd
from watson_developer_cloud import AlchemyLanguageV1
alchemy_language = AlchemyLanguageV1(api_key='Your_Key')

f= open('Your_Dir1', 'a', encoding='utf8')
with open('Your_Dir2','r',encoding='latin1') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a = json.dumps(alchemy_language.combined(text=row, language='english', extract='keywords', sentiment=1),indent=2)
        print(row[0],a)
f.close()