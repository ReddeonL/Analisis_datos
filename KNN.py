#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# carga el dataset
df=pd.read_csv('C:/Users/Home/OneDrive - Universidad Nacional Abierta y a Distancia/unad/9 semestre/analisis de datos/entrega 4/Raw-Data.csv')
#remover columnnas innesearias
df=df.drop(['Severity'],axis=1)
#reemplazar valores no numericos con la media
for col in df.columns:
    if df[col].dtype=='object':
        df[col]=pd.to_numeric(df[col],errors='coerce')
        df[col]=df[col].fillna(df[col].median())
#convertir valores string a numericos
df=pd.get_dummies(df,columns=['Gender','Contact'])
#separar los datos en traing y testing
x_train,x_test,y_train,y_test=train_test_split(df.drop('Severity',axis=1), df['Severity'],test_size=0.4,random_state=4)

#crear un KNN calisicador con k=4
knn=kNeighborsClassifier(n_neighbors=4)

#train the classifier
knn.fit(x_train,y_train)

#hacer prediccion sobre el training set
y_pred=knn.predict(x_test)

#calcular la precision del clasificador
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy",accuracy)


# In[ ]:





# In[ ]:




