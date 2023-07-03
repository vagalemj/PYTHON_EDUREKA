from collections import Counter

a=[1,2,2,1,3,4,5,5,5,3,1,2,3,8,8,1,7]
b=Counter(a)        #counts the number of occurance if values inside list

print(b)

print(list(b.elements()))   #returns list containing all the elements (ordered)

print(b.most_common())      #return sorted list with the count

sub={2:1,1:1}

print(b.subtract(sub))  #subtraction of number of elements

print(b.most_common())

print(b.keys())     #dictionary keys