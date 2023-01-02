#f=open("cipherschools.txt","r")
#print(f.read())
#delete text
#import os
#os.remove("dummy.txt")

#import os
#if os.path.exists("dummy.txt"):
 #   os.remove("dummy.txt")
#else:
 # print("file not  in exist")
  
#exception Hsndling
#try:block lets you to test code
#except:error is handled here
#else:
#finally: 

#try:
 #   print(a)
#except:
 #   print("not defined")
    
try:
    print(a)
except NameError:
    print("a is not defined")
except:
    print("Something is not working")
    
    
#try:
#    a=x/y
#except:
#    print("denominator connot be zero")
#except:
#    print("hello world")
    
try:
    print(a)
except:
    print("a is not defined")
finally:
    print("మనల్ని ఎవడురా ఆపేది")
    
try:
    f=open("dummy.txt")
    try:
        f.write("Hello World")
    except:
        print("Error during writing")
    finally:
        f.close()
except:
    print("Error in opening file")
    
try:
    print("Hello Class")
except:
    print("Error")
else:
    print("Working")
    
f1=open("cs.jfif","rb")
print(f1.read)
f1=open("cs.ifif","wb")
    


