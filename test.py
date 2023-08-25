#import math
#import numpy as np 

def asc_des_none(lst, s):

    if(s == "Desc"):
  
        return sorted(lst)
    elif (s == "Asc"):

        return sorted(lst,reverse=True)
    else:
        return lst


#print(asc_des_none([1,3,2,4],"asc"))



def V_DAC(value):
    DAC =(value/1023)*5
    DACround = round(DAC,2)
    return DACround

#print(V_DAC(1000))



def factorial(intereger):
    total =1
    for i in range(1,intereger+1):
        total = i*total

    return total



#print(factorial(13))


def billableDay(days):

    if(days<=32):
        return 0
    elif(days >=33 and days <=40):
        tempVal = days - 32
        outpay = tempVal *325
        return outpay
    elif(days >= 41 and days <= 48):
        tempVal= days -32
        outpay = (8*325) + tempVal*550
        return outpay
    elif(days >= 48):
        tempVal = days - 48
        outpay = (8*325) + 8*550 + tempVal*600
        return outpay


#print(billableDay(50))


def dis(cost,prosent):

    sale =(cost*prosent)/100
    total = cost-sale
    return round(total,2)


#print(dis(100,75))



def fizz_buzz(number):
    if(number%3==0 and number%5==0):
        return "FizzBuzz"
    elif (number%3==0):
        return "Fizz"
    elif(number%5 == 0 ):
        return "Buzz"
    else:
        return1 = str(number)
        return return1
    



#print(fizz_buzz(4))



def fib_fast(numb):
    a = 0
    b = 1


    for i in range(numb+1):
        if i <= 1:
            print(i)
        else: 
            c = a + b
            a = b
            b = c
            print(c)

    return c


print(fib_fast(10))