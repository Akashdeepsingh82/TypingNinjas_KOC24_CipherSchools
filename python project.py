import random
value=random.randint(10,50)
a=value
print("The chosen number from range  is:",a)
print("The properties followed by this number are;")
if a>0:
    print(a,"is a positive number")
elif a<0:
    print(a,"is negative number")
if a%2==0:
    print(a,"is even number")
elif a%2!=0:
    print(a,"is odd number")
count=0
for i in range(2,a):
    if (a%i)==0:
        count+=1
if count>=1:

        print(a,"is composite number")

else:
         print(a,"is prime number")
