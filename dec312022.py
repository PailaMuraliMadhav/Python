# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:45:18 2022

@author: singam s3
"""

#Regular expression:
#1:search word
import re
str="My name is Murali"
a=re.search("^My.*Murali$",str)
if a:
    print("Search exists")
else:
    print("Search doesn't exists")
    
#2
import re
str="My name is Murali"
a=re.findall("M",str)#findall-particular charecters or keyword exists or not
print(a)#only Capital or small

#3:first white space will be splitted by comma(two parts)
import re
str="My name is Murali"
a=re.split("\s",str,1)
print(a)

#4:enter a number or character btw spaces(sub)
import re
str="My name is Murali"
a=re.sub("\s","2",str,2)
print(a)

#5