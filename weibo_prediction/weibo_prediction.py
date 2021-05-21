#Usable
import re
import datetime
import string, os 
import pandas as pd

# Import Data
curr_dir = './Weibo Data/Weibo Data/weibo_train_data(new)/'
name = './weibo_train_data_aux.txt'
fname = name # curr_dir+name
file_data = []
data = pd.read_csv(fname, delimiter = "\t", encoding="utf8")#, header=None) 
"""
    for i in range(0,len(data[0])):
        uid = data[0][i]
        mid = data[1][i]
        time = data[2][i]
        forward_count = data[3][i]
        comment_count = data[4][i]
        like_count = data[5][i]
        content = data[6][i]
"""
# Clean the data
# Remove mentions, punctuation, #, emojis and links

#df_train = pd.read_csv('/Users/jackcapt/Documents/BIT STUFF/Python script/Weibo Data/weibo_train_data.txt', delimiter = "\t", encoding="utf-8")
df = pd.DataFrame(data) # df_train
df = df.rename(columns={"d38e9bed5d98110dc2489d0d1cac3c2a": "uid", "7d45833d9865727a88b960b0603c19f6": "mid", "2015-02-23 17:41:29": "time","0":"forward_count","0.1":"comment_count","0.2":"like_count","丽江旅游(sz002033)#股票##炒股##财经##理财##投资#推荐包赢股，盈利对半分成，不算本金，群：46251412":"content"}, errors="raise")
df.head()

context = df[['content']]
context.head()

def clean_data(context):
#replace URL of a text
    #Remove links
    context['content'] = context['content'].str.replace('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '')
    #Remove Emoji
    context['content'] = context['content'].str.replace('\[.{0,12}\]', '')
    #Remove Hashtags
    tags = re.findall("#(.{0,30})#",str(context))
    context['content'] = context['content'].str.replace('#(.{0,30})#', '')
    #Extract&Remove EnglishCharacters
    english = re.findall("[a-z]+",str(context))
    context['content'] = context['content'].str.replace('[a-z]+', '')
    #Extract and remove Mentions
    at = re.findall("@([^@]{0,30})\s",str(context))
    context['content'] = context['content'].str.replace('@([^@]{0,30})\s', '')
    at+= re.findall("@([^@]{0,30})）",str(context))
    context['content'] = context['content'].str.replace('@([^@]{0,30})）', '')
    #Remove Spaces
    context['content'] = context['content'].str.replace('\s', '')
    #Remove Digits
    context['content'] = context['content'].str.replace('\d', '')
    #Remove……
    context['content'] = context['content'].str.replace('\.*', '')
    #Remove Punctuation
    context['content'] = context['content'].str.replace('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+', '')
    context['content'] = context['content'].str.replace('[【】╮╯▽╰╭★→「」]+', '')
    context['content'] = context['content'].str.replace('！，❤。～《》：（）【】「」？”“；：、', '')

clean_data(context)
print(context['content']);

context.head()

cleaned_data = pd.concat([df,context], axis=1, sort=False)
cleaned_data.head()

# cleaned_data.to_csv('/Users/jackcapt/Documents/BIT STUFF/Python script/Weibo Data/df_tranClean.csv', index=False)

# Sentiment analysis

# Input values to the algorithm: content, keywords, sentiments, date and hour
# LSTM network

# Output count of likes, comments and forward count