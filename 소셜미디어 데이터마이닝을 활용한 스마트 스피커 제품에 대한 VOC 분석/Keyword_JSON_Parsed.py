import json
import requests
import csv
from collections import OrderedDict
from pprint import pprint
from os.path import join, dirname
import pandas as pd
from watson_developer_cloud import AlchemyLanguageV1
alchemy_language = AlchemyLanguageV1(api_key='Your_Key')

f= open('Directory1', 'a', encoding='utf8')
with open('Directory2','r',encoding='latin1') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a =json.dumps(alchemy_language.combined(text=row, language='english', extract='keywords', sentiment=1))
        a = json.loads(a)
        try:
            print('ID : ',row[0])
            pprint(a['keywords'][0]['text'])
        except IndexError :
            pass
        except KeyError:
            pass

        print(' ')
f.close()