#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import-packages: Might be included in the requirements.txt after I complete with all tasks
import pandas as pd
import numpy as np 
from numpy import random
import math
from datetime import datetime
import matplotlib.pyplot as plt 
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')
import sys
import re
import patsy as pt
import pymc3 as pm
plt.style.use('seaborn-darkgrid')
from sklearn.model_selection import train_test_split

# ## Simulate time-series data 

# In[3]:


import random
def constrained_sum_sample_pos(n, total):
    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def constrained_sum_sample_nonneg(n, total):
    """Return a randomly chosen list of n nonnegative integers summing to total.
    Each such list is equally likely to occur."""

    return [x - 1 for x in constrained_sum_sample_pos(n, total + n)]

def simple_gen(x): #generate a random dataset with specified variables
    random.seed(x)
    #time-series
    date = pd.date_range(start='1/1/2020', end='3/27/2020', freq='D')
    df = pd.DataFrame(date, columns=['date'])
    #target variables: reported cases
    df['actual']=np.random.randint(0,1000,size=len(date))
    #variables: number of patients with pre-existed medical conditions
    pre=[]
    for case in df['actual']:
        a=np.random.randint(1,case)
        
        pre.append(a)
    df['reported']=pre
    #variables: number of patients recorded from different areas, there are 3 types of areas: 
    
    h1=[] 
    h2=[] 
    h3=[] #h1 for highly infective area, h2 for areas with medium infectivity and h3 for low 

    for i in df['reported']: 
        a1, a2, a3 = constrained_sum_sample_nonneg(3,i)
        h1.append(a1)
        h2.append(a2)
        h3.append(a3)
    df['area1']=h1
    df['area2']=h2
    df['area3']=h3
    #variables: temperatures of the day
    
    high=[]
    low=[]
    for i in range(len(df['date'])):
        c=np.random.randint(10,30)
        d=np.random.randint(10,30)
        if c>d: 
            high.append(c)
            low.append(d)
        else: 
            high.append(d)
            low.append(c)
    df['HighTemp']=high
    df['LowTemp']=low
    #number of deaths: 
    df['death']=np.random.randint(0,50,size=len(date))
    
    return df


# ## Simulate Panel Data 
# Goal is to assist the probit regression 

# In[15]:


def get_file():
    df=pd.read_csv(r'D3.csv')
    a=10.986409919681789
    b=171.91508511054587
    df['height']=df['height']*a+b       
    return df

def get_panel_data(): 
    df = get_file()
    df['height']=df.height.round()
    df['contacts_count']=df.contacts_count.round()
    #Height is Z-score Normalized  => need to change => reverse Z-score and convert to int32
    # contacts_count in assessment 1 have been imputed with MEAN => round it into int32
    mapping = {'yes':1, 'no':0, 'blank':np.nan}
    df['insurance']=df.insurance.map(mapping)
    df['insurance'].fillna(df['insurance'].mode()[0], inplace=True)
    secmap={'native':1,'immigrant':0, 'blank':np.nan}
    df['immigrant']=df.immigrant.map(secmap)
    df['immigrant'].fillna(df['immigrant'].mode()[0], inplace=True)
    #Convert data type: 
    convert_dict = {'contacts_count':int, 'height': int,'worried': int, 'immigrant':bool,'insurance':bool,'covid19_positive':bool,'covid19_symptoms':bool,'covid19_contact':bool,'asthma':bool,'kidney_disease':bool,'liver_disease':bool,'compromised_immune':bool,'heart_disease':bool,'lung_disease':bool,'diabetes':bool,'hiv_positive':bool,'hypertension':bool,'other_chronic':bool,'nursing_home':bool,'health_worker':bool}
    df = df.astype(convert_dict) 
    df=df[['height', 'weight', 'insurance', 'immigrant', 'contacts_count',
       'house_count', 'public_transport_count', 'worried', 'covid19_positive',
       'covid19_symptoms']]
    
   
    df = pd.get_dummies(df)
    y = df['covid19_positive']
    X = df.drop(['covid19_positive'], axis=1)
    
    X_mat=X.to_numpy()

    
    # setting random state
    rs = 42

    
    X_train, X_test, y_train, y_test = train_test_split(X_mat, y, test_size=0.29, stratify=y, random_state=rs)

    return df,X,y,X_train, X_test, y_train, y_test
    
def analyse_feature_importance(dm_model, feature_names, n_to_display=20):
    # grab feature importances from the model
    importances = dm_model.feature_importances_
    
    # sort them out in descending order
    indices = np.argsort(importances)
    indices = np.flip(indices, axis=0)

    # limit to 20 features, you can leave this out to print out everything
    indices = indices[:n_to_display]

    for i in indices:
        print(feature_names[i], ':', importances[i])

    
    


# In[4]:





# In[6]:





# In[7]:





# In[8]:





# In[14]:





# In[ ]:




