import pandas as pd
df=pd.read_csv('CovidData.csv')
import numpy as np
def data_split(data,ratio):
    shuffled=np.random.permutation(len(data))
    test_size=int(len(data)*ratio)
    test_indices=shuffled[:test_size]
    train_indices=shuffled[test_size:]
    return data.iloc[train_indices],data.iloc[test_indices]
train,test=data_split(df,0.25)

x_train=train[['Fever','Weakness','Dry Cough','Breathing Difficulty','Sore Throat','Body Pain','NasalBlock','Runny Nose','Diarrhea','Age','Gender']].to_numpy()
x_test=test[['Fever','Weakness','Dry Cough','Breathing Difficulty','Sore Throat','Body Pain','NasalBlock','Runny Nose','Diarrhea','Age','Gender']].to_numpy()
y_train=train[['Virusprob']].to_numpy()
y_test=test[['Virusprob']].to_numpy()

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)

name=input("Hey, Welcome!!\nEnter your Name: ")
covid=[]
age=int(input("Enter your age: "))
gen=int(input("Are you Male or Female, type 1 for Male, 0 for Female: "))
fever=float(input("Enter you temperature: "))
wn=int(input("Do you have weakness??\nType: 1 for YES , 0 for NO: "))
dc=int(input("Do you have dry cough??\nType: 1 for YES , 0 for NO: "))
bd=int(input("Do you have difficulty in breathing??\nType: 1 for YES , 0 for NO: "))
st=int(input("Do you have sore throat??\nType: 1 for YES , 0 for NO: "))
pain=int(input("Do you have body pain??\nType: 1 for YES , 0 for NO: "))
nb=int(input("Do you have nasal blockage??\nType: 1 for YES , 0 for NO: "))
rn=int(input("Do you have runny nose??\nType: 1 for YES , 0 for NO: "))
dia=int(input("Do you have diarrhea??\nType: 1 for YES , 0 for NO: "))
covid.append(fever)
covid.append(wn)
covid.append(dc)
covid.append(bd)
covid.append(st)
covid.append(pain)
covid.append(nb)
covid.append(rn)
covid.append(dia)
covid.append(age)
covid.append(gen)
probability=lr.predict_proba([covid])[0][1]
print("\n")
print(name,"your chances of having/getting infected by COVID-19 is: ",round(probability*100,3),"%")