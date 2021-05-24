import datetime
import string, os 
import pandas as pd

# Import Data
# curr_dir = './Weibo Data/Weibo Data/weibo_train_data(new)/'
name = './tokenized_data.csv'
fname = name # curr_dir+name
data = pd.read_csv(fname, delimiter = "\t", encoding="utf8")#, header=None) 
#print(data)
data = pd.read_csv(fname, encoding="utf8")#, header=None) #delimiter = "\t", 
#data.head() #data.iloc[[0]] #data[['time']] #print(data.dtypes)
data['time'] =  pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S')
print(data[['time'][0]][0])

# Sentiment analysis

# Input values to the algorithm: content, keywords, sentiments, date and hour
# LSTM network

"""
    # Example of LSTM to learn a sequence
    from pandas import DataFrame
    from pandas import concat
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import LSTM
    # create sequence
    length = 10
    sequence = [i/float(length) for i in range(length)]
    print(sequence)
    # create X/y pairs
    df = DataFrame(sequence)
    df = concat([df.shift(1), df], axis=1)
    df.dropna(inplace=True)
    # convert to LSTM friendly format
    values = df.values
    X, y = values[:, 0], values[:, 1]
    X = X.reshape(len(X), 1, 1)
    # 1. define network
    model = Sequential()
    model.add(LSTM(10, input_shape=(1,1)))
    model.add(Dense(1))
    # 2. compile network
    model.compile(optimizer='adam', loss='mean_squared_error')
    # 3. fit network
    history = model.fit(X, y, epochs=1000, batch_size=len(X), verbose=0)
    # 4. evaluate network
    loss = model.evaluate(X, y, verbose=0)
    print(loss)
    # 5. make predictions
    predictions = model.predict(X, verbose=0)
    print(predictions[:, 0])
"""

# Output count of likes, comments and forward count