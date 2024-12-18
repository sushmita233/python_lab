#Q.4) Perform Intersection operation on list
#2 list
list1=[45,76,54,97,44]
list2=[45,77,44,23,40,50]

#intersection of 2 
intersection=list(set(list1) & set(list2))

#output
print("list One: ",list1)
print("list two: ",list2)
print("-------------------")
print("Intersection of the 2 list: ",intersection)
