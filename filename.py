import math
print("hello world")
print("this is another testing sentences")



print(math.sqrt(19))
print(math.log(16,4))

Fox = "ABCDEFGHIJK"
print( Fox[0:1])

print (Fox[3:len(Fox)])

def large_among(a,b,c):
	if(a>b and a>c):
		return a
	elif(b > c):
		return b
	else:
		return c

print (large_among(6,2,3))

# x = "Hello2"
# y = "Hello"
# print(x==y)

lunch = ['chicken','rice','pork','steak',31]
print (lunch[4])
lunch.append(62)
lunch.remove('rice')
print(lunch.index(31))

