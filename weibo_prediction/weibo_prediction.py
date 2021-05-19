import datetime
import string, os 

curr_dir = './Weibo Data/Weibo Data/weibo_train_data(new)/'
name = 'weibo_train_data.txt'
fname = curr_dir+name
file_data = []

with open(fname, encoding="utf8") as f: 
    f.readline()
    for line in f:
        line_split = line.split()

        date = str(line_split[2]) 
        time =  str(line_split[3]) 
        date_time_str = date+' '+time
        date_time = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        forward_count = line_split[4] 
        comment_count = line_split[5] 
        like_count = line_split[6]  
        content = line_split[7:] 

        file_data.append([date_time, int(forward_count), int(comment_count), int(like_count)]) # , str(content)])
print(file_data)



