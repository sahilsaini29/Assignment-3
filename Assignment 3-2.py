#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sum of First n Natural numbers , Ask user for Number.


def myreduce(num):
    ''' This functionm will return sum of n Natural numbers'''
    num_list=list(range(1,number+1))
    sum_of_elements=0
    
    for i in num_list:
        sum_of_elements+=i
        
    return num_list,sum_of_elements

#Input 
print("Input:")
number=int(input("Please insert the number :"))

#Function Execution

output_value=myreduce(number)

#Output
print("Output:")
print("List of First n Natural numbers are:",output_value[0])
print("Sum of List elements are :",output_value[1])


# In[ ]:


# Same Solution can be approached by Built-in reduce() function

print("Input:")
number=int(input("Please insert the number :"))

num_list= list(range(1,(number+1)))
# Import reduce function 
from functools import reduce
sum_of_elements = reduce((lambda x, y: x + y), num_list)

#Output
print("Output:")
print("List of First n Natural numbers are:",num_list)
print("Sum of List elements are :",sum_of_elements)


# In[ ]:


# Filter the even and odd number from list which are multiples  of 5

#Input 

print("Input:")
number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))


def myfilter(num_list):
    '''This function will filter even and odd numbers from list which are multiples of 5 '''
    num_even_list=[]
    num_odd_list=[]
    
    for i in num_list:
        if(i%5==0):
            if(i%2==0):
                num_even_list.append(i)
            else:
                num_odd_list.append(i)
                
    return num_even_list,num_odd_list


#Function Execution
output_value=myfilter(num_list)

#Output

print("Output:")
print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",output_value[0])
print("List of Odd numbers, which are multiples of 5 are:",output_value[1])


# In[ ]:


#Same solution can be approached by built-in filter() function

#Input 

print("Input:")
number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))

num_even_list=list(filter(lambda x: x%2==0,list(filter(lambda x: x%5==0 ,num_list))))
num_odd_list= list(filter(lambda x: x%2!=0,list(filter(lambda x: x%5==0 ,num_list))))

print("Output:")

print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",num_even_list)
print("List of Odd numbers, which are multiples of 5 are:",num_odd_list)


# In[ ]:


#Section 1
word="AcadGild"
#list Comprehension
output_list=[w.upper() for w in list(word)]
print("Output:")
print(output_list)

#Section 2
word_1=list('xyz')
word_2=[x*n for x in word_1 for n in range(1,5) ]
print(word_2)

#Section 3
word_3=[x*n for n in range(1,5) for x in word_1 ]
print(word_3)

#Section 4
number=[2,3,4]
number_1=[[x+n] for x in number for n in range(0,3)]
print(number_1)

#Section 5
number_2=[2,3,4,5]
number_3=[[x+n for n in range(0,4)] for x in number_2 ]
print(number_3)

#Section 6
number_4=[1,2,3]
number_5= [(b,a) for a in number_4 for b in number_4]
print(number_5)


# In[ ]:


def longestWord(word_list):
    '''This function will return longest word from input word list'''
    wordlen=[]
    for w in word_list:
        wordlen.append((len(w),w))
    wordlen.sort()
    return wordlen[-1][-1]

#Input
print("Input:")
word_list=input("Please enter your word: ")
word_list=word_list.split(",")
#function execution
longest_word=longestWord(word_list)
print("Output:")
print(longest_word)

