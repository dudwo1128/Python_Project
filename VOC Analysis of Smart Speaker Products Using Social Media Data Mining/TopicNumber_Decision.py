from LDAscikit import LDAprocess
from LDAscikit import Utils

use_f = 0
df_matrix = Utils.ReadCSV(filename='yourfile', delimiter = ',')
df_matrix = Utils.Edgelist2Matrix(df_matrix)

if use_f == 1:
    DocTopic, TopicWord = LDAprocess.LDAexecute(df_matrix, 11, 1, 10)
    TopicInfo = LDAprocess.TopicInfo(TopicWord)

    Utils.WriteCSV("DocTopic.csv", DocTopic)
    Utils.WriteCSV("TopicWord.csv", TopicWord)
    Utils.WriteCSV("TopicInfo.csv", TopicInfo)
elif use_f == 0:
    result = LDAprocess.TopicDecision(df_matrix, 2, 100, 1, 2)
    Utils.WriteCSV("YourFile", result)
elif use_f == 2:
    Utils.WriteCSV(filename="YourFile", matrix=df_matrix, index=True)