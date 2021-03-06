import numpy as np
import pandas as pd

path = '../JData/'
df = pd.read_csv(path + 'JData_Action_201604.csv')

df.time = df.time.astype('datetime64[ns]')
df.time.max()
# split last five days and other action data
start_time = '2016-04-11 00:00:00'
last_five_days = df[df.time > start_time]
last_five_days.to_csv('last_five_days.csv')
JData_Action_201604 = df.drop(last_five_days.index)
JData_Action_201604.to_csv('JData_Action_201604_without_last_five_days.csv')
# filter out all the buy actions for products of category 8 
last_five_days = pd.read_csv(path+'last_five_days.csv')
last_five_days = last_five_days.loc[(last_five_days['cate'] == 8) & (last_five_days['type'] == 4), ['user_id', 'sku_id']]
last_five_days = last_five_days.drop_duplicates()
last_five_days.to_csv('ground_truth.csv')

# last two days
#end_time = '2016-04-13 00:00:00'
#last_five_days = pd.read_csv(path+'last_five_days.csv')
#last_two_days = last_five_days[last_five_days['time'] <= end_time]
#last_two_days = last_two_days.loc[(last_two_days['cate'] == 8) & (last_two_days['type'] == 4), ['user_id', 'sku_id']]
#last_two_days = last_two_days.drop_duplicates()
#last_two_days.to_csv('ground_truth_2_days.csv')