import json
import requests
import csv
from pprint import pprint
import pandas as pd
import numpy as np
from collections import OrderedDict
from watson_developer_cloud import AlchemyLanguageV1
alchemy_language = AlchemyLanguageV1(api_key="Your_Key")


final = pd.DataFrame(np.nan, index=[0], columns=['text','sentiment','ID'])
with open('Your_Dir1','r',encoding='latin1') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a =json.dumps(alchemy_language.combined(text=row, language='english', extract='keywords', sentiment=1))
        a = json.loads(a)
        try:
            df = pd.DataFrame(a['keywords'])
            df = pd.DataFrame(df[['text','sentiment']])
            df['ID'] = row[0]
        except IndexError:
            pass
        except KeyError:
            pass
        if len(df) > 0:
            final = final.append(df)
        print(final)
final.to_csv('Final_Directory', sep=',', encoding='utf-8')