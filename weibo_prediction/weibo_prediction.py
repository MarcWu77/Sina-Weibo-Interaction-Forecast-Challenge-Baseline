import datetime
import string, os 
import pandas as pd

# Import Data
curr_dir = './Weibo Data/Weibo Data/weibo_train_data(new)/'
name = 'weibo_train_data_aux.txt'
fname = curr_dir+name
file_data = []
data = pd.read_csv(fname, delimiter = "\t", encoding="utf8", header=None) 
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

# Sentiment analysis

# Input values to the algorithm: content, keywords, sentiments, date and hour
# LSTM network

# Output count of likes, comments and forward count