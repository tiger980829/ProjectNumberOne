# sequence = ("99",7,12,33,64)

# print(sequence) 
# print(sequence) 

# wee = (['1','2','3','4'],('1','2','3'))
# print(wee)

# print(wee)

# # wee = ['1','2','3','4']
# print(wee[-2])

# print(len(wee))

# set1 = {'lychee','durain','mango',(2,5,8,11),11}
# print(set1)

# Empty = set()
# Empty.add(666)
# print(Empty)

# Empty.update([777,888,999,(10,20,30,40)])
# print(Empty)

Prime = {2,3,5,7,11,13,17}
NonPrime = {4,6,8,9,10,12,14,15}

print(Prime|NonPrime) # Union of set
print(Prime&NonPrime) # intersect of set
print(Prime - NonPrime) # Difference between two set
print(Prime^NonPrime) # Elements not overlapping => Symmertric Difference