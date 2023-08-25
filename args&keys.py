from typing import Any
#UNPACKING:
    #unpacking a tuble 
first , second =('a','b')
print (first)

    #unpacking a list 
first1 ,sec2 ,*rest =[2 , 3 , 11 , 7 , 6 , 88]
print(first1)
print(sec2)
print(rest)

    #unpacking a dictionary
dict1 = {
    "name": "sara",
    "age" : 26,
    "type" : "female"
}
dict2 = {"ID" : 101, **dict1}
print(dict2)

#VARIABLES ARGUMENTS
def func(*nums:int) -> None :
    for number in nums :
        print (number)

func(6,3,7,10)    

def func2(**kwargs : Any) ->None:
    for k , v in kwargs.items():
        if v > 300: print(f"{k} is too much")
        else: print(f"{k} is good")

func2(pizza = 250, burger = 400 , icecream= 25)        