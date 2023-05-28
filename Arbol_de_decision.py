#!/usr/bin/env python
# coding: utf-8

# In[11]:


#arbol de desiciones
#arboles de decicion en python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# In[15]:


df=pd.read_csv('C:/Users/Home/OneDrive - Universidad Nacional Abierta y a Distancia/unad/9 semestre/analisis de datos/entrega 4/covid.csv',
engine='python',index_col=0)


# In[16]:


df.head()


# In[17]:


df.info()


# In[21]:


#Eliminar filas faltantes 
df.dropna(inplace=True)
#variable predictora
x=df.iloc[:,:-1]

#variable a predecir
y=df.iloc[:,-1]
#convertir  variables categhoricas en variables numericas
x=pd.get_dummies(x)


# In[22]:


#dividir el conjunto de datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)


# In[23]:


#crear un modelo de arbol de decision y entrenarlo con el conjunto de datos de entrenamientto
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)


# In[24]:


#Evaluar el modelo con el conjunto de datos de prueba
score=clf.score(x_test,y_test)
print("Accuracy: %.2f%%" % (score*100.0))


# In[ ]:




