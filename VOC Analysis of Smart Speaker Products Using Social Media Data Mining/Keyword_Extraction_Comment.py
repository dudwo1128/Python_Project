import json
import csv
import pandas as pd
import numpy as np
from watson_developer_cloud import AlchemyLanguageV1, WatsonApiException
import watson_developer_cloud

# alchemy key input
alchemy_language = AlchemyLanguageV1(api_key="Your_Key")

# Empty DataFrame
final = pd.DataFrame(np.nan, index=[0], columns=['text','sentiment','ID'])

# Get CSV file to use
with open('Directory','r',encoding='latin1') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Specifying the data you want to import through api (ex. keywords, emotional analysis scores)
        # Value returns in json form
        a = json.dumps(alchemy_language.combined(text=row, language='english', extract='keywords', sentiment=1))
        a = json.loads(a)

        # Use the pprint to check the json imported
        # pprint(json.loads(alchemy_language.combined(text=row, language='english', extract='keywords', sentiment=1),object_pairs_hook=OrderedDict))

        try:
            # Recall only keyword information and save it to a data frame
            df = pd.DataFrame(a['keywords'])

            # Recall text, current columns from above data frames and save them to a dataframe
            df = pd.DataFrame(df[['text','sentiment']])

            # Adding an ID matrix to a data frame
            df['ID'] = row[0]

        # Exception processing: Skip if there is no keyword in the document

        except WatsonApiException:
            pass
        except IndexError:
            pass
        # Exception: Pass if there is an emotional type in the document but no score
        except KeyError:
            pass



        # Add to final data frame if above data frame is not empty
        if len(df) > 0:
            final = final.append(df)
            #print(df)
        print(final)
final.to_csv('Final_Directory', sep=',', encoding='utf-8')