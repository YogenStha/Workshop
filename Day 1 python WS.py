# #lists
# a=[ 
#    {'name':'Ram',
#     'age':20},
#    {'name':'Shyam',
#     'age':40}
#    ]
# #for loop for prinnting list
# for x in a:
#print(x)
# #appending in lists    
# a.append({"name":"saurab","age":"50"})
# for x in a:
#     print(x)
# #popping in list
# # a.pop(2)
# for x in a:
#    print(x)
# #removing sprecifif data in list
# a.remove({'name':'Shyam',
#     'age':40})
# for x in a:
#     print(x)
#arr=[]
#couting the number of occurences
# x=1
# while(x<=20):
#    if(x%2!=0):
#     arr.append(x)
#    x=x+1  
# print("ODD NO:",arr)
# arr.sort(reverse=True)
# print("Odd Rev:",arr)

# for index,x in enumerate(range(1,20,3)):
#    print(index,x)

# arr2=[]
# print(len(string_arr))
# length = string_arr.__len__()
# x=1
# while(x<=length):
#    if(x%2==0):
#      arr2.append(x)
#    x=x+1  
# print(arr2)
# string_arr=["Ram","hari","John","JOHN DOE"]
# string_arr[1] = string_arr[1] +" "+ "Prasai"
# print(string_arr)
# string_arr.insert(2,'test')
# print(string_arr)
      
# for index,value in enumerate(string_arr):
#     print(f"This is {index} index and value is {value}")
    
# for index,val in enumerate(string_arr):
#     if(index%2==0):
#         print(val)
       
# dynamic_value= int(input("Enter any  number:"))
# print(dynamic_value)       

# WAP to convert celcius to farhenheit:

# #anonymous function
# anomFunc = lambda x,y:x+y
# print(anomFunc(4,5))

# def closure(x):
#     a=6
#     def innerFunc(y):
#         return x+y+6
#     return innerFunc

# closure_instance=closure(4)
# result=closure_instance(5)
# print(f"Result is {result}")

# def Divisionfunc(a,b):
#      try:
#         result=a/b
#         if a==5:
#             raise ZeroDivisionError("5 cannot be used")
#         return result
#      except ZeroDivisionError:
#          print("Error! cannot be divided by zero")
#          return None
#      except Exception as e:
#          print("Internet error!!!",e)
#          return None
# Divisionfunc(5,1)        

# value_a=int(input("Enter the number to be divided:"))
# value_b=int(input("Enter the value to divide by:"))

# print(Divisionfunc(value_a,value_b))
# def converter(celcius):
    
#     farhen=((9*celcius)/5)+32
#     print(f"{celcius}C is equal to {farhen}F")
    
# def converter2(farhen):
#     celcius=((farhen-32)*9)/5
#     print(f"farhenheit to celcius is {celcius}")
    
# choice=int(input("Choose one option:\n 1.celcius to farhenheit \n 2.Farhenheit to celcius\n"))   
# if(choice==1):
#     cel=int(input("Enter celcius value to be converted:"))
#     converter(cel)
# else:
#     far=int(input("Enter Farhenheit value to be converted:"))
#     converter(far)
import asyncio as a 
async def getData():
    print("Hello")
    await a.sleep(2)
    print("hi")

a.run(getData())