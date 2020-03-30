s=input()
lst=['Sunny','Cloudy','Rainy']
index=lst.index(s)
newIndex=(index+1)%len(lst)
print(lst[newIndex])
