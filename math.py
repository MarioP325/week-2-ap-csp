x=3
y=5
temp=x
x=y
y=temp
print(x,y)
print(x+y)
yourlist=(20,40,60,80)
mylist=(10,30,50,70)
yourlist=mylist
print(yourlist)
print(f"you have ", x, "dollars with the current rate that it will be", x*y, "dollars")
a=True
b=False
c=True
a=not a or b and c
c= c and a
print(a)
print(b)
print(c)
response=input("Are you doing well")
if response=="yes": print("good")
if response=="no": print("sorry to hear")
word=input("write a word")
print(len(word))
count=len(word)
if count>=7: print("This is too long")
else: print("good enough length")