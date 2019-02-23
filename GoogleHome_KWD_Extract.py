# GoogleHome
import csv
import watson_developer_cloud
import json
from watson_developer_cloud import AlchemyLanguageV1, WatsonApiException

ALCHEMY_KEY = [["Your_Key1"], ["Your_Key2"],
               ["Your_key3"], ["Your_Key4"],
               ["Your_Key5"]]
key_number = 0
alchemy_language = AlchemyLanguageV1(api_key=ALCHEMY_KEY[0])


fr = open("Your_Directory1", "r", newline = '')
reader = csv.reader(fr)
last_doc_num = 0
for row in reader:
	last_doc_num = int(row[0])
print(last_doc_num)


fr = open("Your_Directory2", 'r', encoding='latin1')
fw = open("Your_Directory1", "a", newline = '')
reader = csv.reader(fr)
writer = csv.writer(fw)

print("Start")
for i, row in enumerate(reader):
	if i > 80000:
		break

	doc_num = int(row[0])
	doc_text = str(row[1])

	def GetKWD(row):
		alchemy_return = alchemy_language.combined(text=doc_text, language='english', extract='keywords', sentiment = 1)
		my_json = json.dumps(alchemy_return)
		my_json = json.loads(my_json)
		for now_kwd in my_json['keywords']:
			keyword = now_kwd['text']
			type = now_kwd['sentiment']['type']
			score = '0'
			if 'score' in now_kwd['sentiment'].keys():
				score = now_kwd['sentiment']['score']

			len_1 = len(doc_text)
			len_2 = len(doc_text.replace(keyword, ""))
			tf = int((len_1 - len_2) / len(keyword))
			writer.writerow([doc_num, keyword, tf, type, score])

	
	print("doc_num: " + str(doc_num))
	if doc_num <= last_doc_num:
		continue
	
	try:
		GetKWD(row)
	except Exception as ex:
		print(ex.args[0])
		if ex.args[0] == "daily-transaction-limit-exceeded":
			key_number += 1
			if key_number < len(ALCHEMY_KEY):
				alchemy_language = AlchemyLanguageV1(api_key=ALCHEMY_KEY[key_number])
				GetKWD(row)

				continue
			else:
				exit()
		else:
			print("UNKNOWN ERR")