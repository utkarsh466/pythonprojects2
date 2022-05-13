import statistics as st
import pandas as pd
import random
import plotly.figure_factory as ff

df=pd.read_csv('StudentsPerformance.csv')
# data=df['math score'].tolist()
data=df['reading score'].tolist()
# data=df['writing score'].tolist()

# fig=ff.create_distplot([data],['data'],show_hist=False)
# fig.show()

mean=st.mean(data)
median=st.median(data)
mode=st.mode(data)
stdev=st.stdev(data)

print(f'Mean of this data:- {mean}')
print(f'Median of this data:- {median}')
print(f'Mode of this data:- {mode}')
print(f'Standard deviation of this data:- {stdev}')

sampled_mean_list=[]
for i in range(1000):
    sampled_list=[]
    for i in range(100):
        randomIndex=random.randint(0,len(data)-1)
        sampled_list.append(data[randomIndex])
    sampled_mean_list.append(st.mean(sampled_list))        

sampled_mean=st.mean(sampled_mean_list)
sampled_median=st.median(sampled_mean_list)
sampled_mode=st.mode(sampled_mean_list)
sampled_stdev=st.stdev(sampled_mean_list)
# print('----------------------------------------------------------------')
# print(f'Sampled mean {sampled_mean}')
# print(f'Sampled median {sampled_median}')
# print(f'Sampled mode {sampled_mode}')
# print(f'Sampled stdev {sampled_stdev}')


first_stdev1=mean-stdev
first_stdev2=mean+stdev
counter=0

for i in data:
    if first_stdev1<i<first_stdev2:
        counter+=1

print(f'{counter*100/len(data)}% of data lies within 1 standard deviation')

second_stdev1=mean-stdev*2
second_stdev2=mean+stdev*2
counter=0
for i in data:
    if second_stdev1<i<second_stdev2:
        counter+=1

print(f'{counter*100/len(data)}% of data lies within 2 standard deviation')        

third_stdev1=mean-stdev*3
third_stdev2=mean+stdev*3
counter=0
for i in data:
    if third_stdev1<i<third_stdev2:
        counter+=1

print(f'{counter*100/len(data)}% of data lies within 3 standard deviation')        