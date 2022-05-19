import statistics as st
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('medium_data2.csv')
data=df['reading_time'].tolist()

mean = st.mean(data)
stdev =st.stdev(data)


sampled_list=[]
for i in range(1000):
    samples=[]

    for i in range(100):
        randomIndex=random.randint(0,len(data)-1)
        samples.append(data[randomIndex])
    sampled_list.append(st.mean(samples))        

sampled_mean=st.mean(sampled_list)
stdev_sample=st.stdev(sampled_list)



new_df=pd.read_csv('sample_2.csv')
new_data=new_df['reading_time'].tolist()

new_sample_mean=st.mean(new_data)

new_fig=ff.create_distplot([new_data],['New sample'],show_hist=False)
new_fig.show()
zscore=(new_sample_mean-sampled_mean)/stdev_sample

print(mean)
print(sampled_mean)
print(new_sample_mean)

print(f'The z score is = {zscore}')


fig=ff.create_distplot([sampled_list],['Sampled means'],show_hist=False)

first_stdev1=mean-stdev
first_stdev2=mean+stdev


second_stdev1=mean-stdev*2
second_stdev2=mean+stdev*2

third_stdev1=mean-stdev*3
third_stdev2=mean+stdev*3



fig.add_trace(go.Scatter(x=[first_stdev1,first_stdev1],y=[0,1.2],mode="lines",name='First standard deviation start'))
fig.add_trace(go.Scatter(x=[first_stdev2,first_stdev2],y=[0,1.2],mode='lines',name="First standard deviation end"))
fig.add_trace(go.Scatter(x=[second_stdev1,second_stdev1],y=[0,1.2],mode="lines",name='Second standard deviation start'))
fig.add_trace(go.Scatter(x=[second_stdev2,second_stdev2],y=[0,1.2],mode='lines',name="Second standard deviation end"))
fig.add_trace(go.Scatter(x=[third_stdev1,third_stdev1],y=[0,1.2],mode="lines",name='Third standard deviation start'))
fig.add_trace(go.Scatter(x=[third_stdev2,third_stdev2],y=[0,1.2],mode='lines',name="Third standard deviation end"))
fig.add_trace(go.Scatter(x=[new_sample_mean,new_sample_mean],y=[0,1.2],mode='lines',name='New mean'))


fig.show()

