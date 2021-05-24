import snownlp
from snownlp import SnowNLP
import pandas as pd
cleaned_data = pd.read_csv('C:/Users/hpena/cleaned_data.csv', encoding='utf-8')
print(cleaned_data.shape[0])
cleaned_data.dropna(how='any', axis='index', inplace=True)
print(cleaned_data.shape[0])
sentiment = []
for text in cleaned_data["cleaned_content"]:
    s = SnowNLP(text)
    sentiment.append(s.sentiments)

#Save Sentiments

sent = pd.DataFrame(sentiment)
sentiment_data = pd.concat([cleaned_data, sent], axis=1, sort=False)
sentiment_data.to_csv('C:/Users/hpena/sentiment_data.csv', index=False)    

