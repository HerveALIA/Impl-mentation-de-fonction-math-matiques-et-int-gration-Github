#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2.Création de fonction comportant des modules de gestions des exceptions
    #Je choisis de travailler avec la première fonction
x=input("Veuillez saisir un valeur numérique:")

def Polynome (x):
    while(type(x)==str):
        print("Impossibilité de saisir un str dans la fonction")
        x=int(input("Veuillez saisir un valeur numérique:"))
    print((x**3)-(1.5*(x**2))-(6*x)+5)
    
Polynome(x)


# In[ ]:


#Saisie un nombre complexe

def is_cplx(X):
  #### Si les nombre entrée sont complexes
  if (type(X) == complex) or (type(X) ==int):
     X = x.real #### On prend la partie réelle du nombre et on réaffecte la valeur de a avec
  


# In[ ]:


#Saisie d'un nombre négatif,d'un très grand nombre, d'un très petit nombre

def neg(X):
  #### Si l'une des deux valeurs est négative alors
  if (X < 0) 
    X = abs(x)
    #x = abs(x)    #### on passe cette valeur à la valeur absolue
    return (X) #### On calcul c
  elif (x > 0) 
    X = abs(x) 
    return (x)
  else:
    X = abs(x)
  
    

