# Debug Code``
# Now we will debug the code related to data types.

# A.
a = "Megha"
print a#error:missing parantheses in print function
#correct code:
a = "Megha"
print (a)
 
# B.
a="navgurukul"
b= 2016
print(a+"," + b + "me shuru hua tha")#error:we cannot concatenate string to integer
#correct code:
a="navgurukul"
b= 2016
print(a +","+str(b) + "me shuru hua tha")
 
# C.
a="navgurukul"
b=13
print(a+b)#error:cannot concatenate string to int
#correct code:
a="navgurukul"
b=13
print(a+str(b))
 
# D.
a="12"
b=13.1
print(a+b)#error:cannot concatenate string to float
#correct code:
a="12"
b=13.1
print(int(a)+b)

 
# E.
a = boolean("")#error:it's  not boolean it's bool
b = boolean(" ")
print(a+b)
#correct code:
a = bool("")
b = bool(" ")
