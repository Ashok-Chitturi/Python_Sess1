#!/usr/bin/env python
# coding: utf-8

# In[3]:


str = "I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"

#1length of the string
len(str)


# In[4]:


#2 Lower the text in the string.
str.lower()


# In[15]:


#3
arr = ''''"'''

for x in str.lower(): 
    if x in arr: 
        string = string.replace(x, "") 

        
# Print string without punctuation 
print(str) 


# In[25]:


#5  Python code to find frequency of each word 
def freq(str): 
    str = str.split()          
    str2 = [] 
  
    for i in str:              
  
        # checking for the duplicacy 
        if i not in str2: 
  
            # insert value in str2 
            str2.append(i)  
              
    for i in range(0, len(str2)): 
  
        # count the frequency of each word(present  
        # in str2) in str and print 
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))   
        
freq(str)


# In[8]:


#7change the word "Supervised" to "Unsupervised" in the string
str1 = "I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"

arr = []
arr2 = ""
str1 = str1.split()

for i in str1:
    i = i.replace("Supervised","Unsupervised",1)
    arr.append(i)
    arr2+=i+" "
print (arr)
print (arr2)


# In[32]:


AI_companies = ['Amazon','Facebook','HiSilicon','Google','Apple','Microsoft','SenseTime']

#Sort the list in ascending order
AI_companies.sort()
print (AI_companies)


# In[33]:


#Add multiple companies at once 'Nvidia', 'OpenAI' , 'Qualcomm' and 'Reliance' to the list
arr = ["Nvidia","OpenAI","Qualcomm","Reliance"]
for i in arr:
    AI_companies.append(i)
print (AI_companies)


# In[35]:


#Lower the list using List comprehension
AI_companies = [i.lower() for i in AI_companies]
print (AI_companies)


# In[36]:


AI_companies.remove('reliance')

print (AI_companies)


# In[ ]:


AI_companies1 = ['Amazon', 'Apple', 'Facebook', 'Google', 'HiSilicon', 'Microsoft', 'SenseTime', 'Nvidia', 'OpenAI', 'Qualcomm', 'Reliance']
AI_companies1

