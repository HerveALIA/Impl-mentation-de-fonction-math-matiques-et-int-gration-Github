#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Projet :
#Création de fonction mathématiques simples en python : 


# In[3]:


#a: Implémentons la fonction polynomiale ci-dessus


# In[1]:


def Polynome (x):
    print((x**3)-(1.5*(x**2))-(6*x)+5)
Polynome (5)


# In[ ]:


#b): Implémenter la fonction factorielle (Approche récursive ou classique) :


# In[24]:



def Factorielle(n):
    factor = 1
    if (n==0):
        return 1
    else:
        for i in range(1,n+1):
            factor = factor * i
        print (factor)
Factorielle(5)


# In[ ]:


#c) Test du code :Implémentation de la suite de Fibonnaci


# In[2]:


def fibonacci(n):
    if(n == 0):
        return n
    if(n == 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
print("La suite de fibonacci est: ")
for i in range(6):
    print(fibonacci(i))


# In[ ]:




