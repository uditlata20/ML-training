import tkinter as ttk
from turtle import title
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
import os
print('Location is: ',os.getcwd(),'\n\n\\n')

app=ttk.Tk()
app.title('Recommendation System')
app.geometry('400x400')

cols=['user_id','movie_id','rating','ts']
df= pd.read_csv('u.data',sep='\t',names=cols).drop('ts',axis=1)
item_cols=['movie_id','title']+[str(i) for i in range(22)]
df1=pd.read_csv('u.item',sep='|',names=item_cols,encoding = "ISO-8859-1")[['movie_id','title']]
movie=pd.merge(df, df1, on='movie_id')  

result=ttk.Variable(app)
box=ttk.Listbox(app, height=10)
for tytle in ['title'].unique():
    box.insert(ttk.END,title)

#box.grid(row=0,column=0)
box.pack(side='left',fill='y')
#box.place(x=10,y=10)

scroll=ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(yscrollcommand=scroll.set)
scroll.pack

box.place(x=10,y=10)
import tkinter as ttk
from turtle import title
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
import os
print('Location is: ',os.getcwd(),'\n\n\\n')

app=ttk.Tk()
app.title('Recommendation System')
app.geometry('400x400')

cols=['user_id','movie_id','rating','ts']
df= pd.read_csv('u.data',sep='\t',names=cols).drop('ts',axis=1)
item_cols=['movie_id','title']+[str(i) for i in range(22)]
df1=pd.read_csv('u.item',sep='|',names=item_cols,encoding = "ISO-8859-1")[['movie_id','title']]
movie=pd.merge(df, df1, on='movie_id')  

result=ttk.Variable(app)
box=ttk.Listbox(app, height=10)
for tytle in ['title'].unique():
    box.insert(ttk.END,title)

#box.grid(row=0,column=0)
box.pack(side='left',fill='y')
#box.place(x=10,y=10)

scroll=ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(yscrollcommand=scroll.set)
scroll.pack

box.place(x=10,y=10)
import tkinter as ttk
from turtle import title
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
import os
print('Location is: ',os.getcwd(),'\n\n\\n')

app=ttk.Tk()
app.title('Recommendation System')
app.geometry('400x400')

cols=['user_id','movie_id','rating','ts']
df= pd.read_csv('u.data',sep='\t',names=cols).drop('ts',axis=1)
item_cols=['movie_id','title']+[str(i) for i in range(22)]
df1=pd.read_csv('u.item',sep='|',names=item_cols,encoding = "ISO-8859-1")[['movie_id','title']]
movie=pd.merge(df, df1, on='movie_id')  

result=ttk.Variable(app)
box=ttk.Listbox(app, height=10)
for tytle in ['title'].unique():
    box.insert(ttk.END,title)

#box.grid(row=0,column=0)
box.pack(side='left',fill='y')
#box.place(x=10,y=10)

scroll=ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(yscrollcommand=scroll.set)
scroll.pack

box.place(x=10,y=10)