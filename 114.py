import pandas as pd
import statistics as st
import plotly.express as px
import numpy as np

df=pd.read_csv('main.csv')


fig=px.scatter(df,x='TOEFL Score',y='Chance of Admit')
fig.show()


a=np.array(df['TOEFL Score'])
b=np.array(df['Chance of Admit'])

m,c =np.polyfit(a,b,1)

print(f'M is :-{m}')
print(f'C is :-{c}')

y=[]

for i in df['TOEFL Score']:
    y_val=m*i+c
    y.append(y_val)

fig=px.scatter(df,'TOEFL Score','Chance of Admit')
fig.update_layout(
    shapes=[
        dict(
            y0=min(y),
            y1=max(y),
            x0=min(df['TOEFL Score']),
            x1=max(df['TOEFL Score']),
            type='line'

        )
    ]
)
fig.show()

#   Code for prediction

x=250
y=m*x+c
print(f'Chances of admit if the TOEFL score {x} is {y}')
