#this is a program that shows the basics of working with list

friends = ["Kevin", "Karen", "Jim", "oscar", "samuel"] #list of strings that contains names, with list we can store multiple values in a single variable
print(friends) #print the list

#to access a particular item in the list, we use the index of the item, where the index starts from 0 for the first item
print(friends[0]) #print the first item in the list
print(friends[1]) #print the second item in the list
print(friends[2]) #print the third item in the list

#to access the last item in the list, we can use negative index, where -1 is the last item in the list
print(friends[-1]) #print the last item in the list

#to access a range of items in the list, we can use the colon operator
print(friends[1:]) #print all the items in the list from the second item to the last item

#to access a range of items in the list, we can use the colon operator
print(friends[1:3]) #print all the items in the list from the second item to the third item

#to modify an item in the list, we can use the index of the item
friends[1] = "Mike" #change the second item in the list to Mike
print(friends) #print the list

#list functions
lucky_numbers = [4, 8, 15, 16, 23, 42] #list of integers
print(lucky_numbers) #print the list

#the extend function allows you to add/append another list to the end of the list
friends.extend(lucky_numbers) #add the lucky_numbers list to the end of the friends list
print(friends) #print the list

#the append function allows you to add/append an item to the end of the list, it can only add one item at a time and it will add the item to the end of the list
friends.append("Creed") #add Creed to the end of the friends list
print(friends) #print the list

#another fucntion to use is the insert function, it allows you to add an item to a particular index in the list and it takes two arguments, the first is the index and the second is the item to be added
friends.insert(1, "Kelly") #add Kelly to the second index of the friends list
print(friends) #print the list

#the remove function allows you to remove an item from the list and it takes one argument, the item to be removed
friends.remove("Jim") #remove Jim from the friends list
print(friends) #print the list

#you can also remove all the items in the list using the clear function
friends.clear() #remove all the items in the friends list, this will print an empty list, but the list is still there, which is different from deleting the list
print(friends) #print the list

#pop function allows you to remove the last item in the list
friends = ["Kevin", "Karen", "Jim", "oscar", "samuel", "jim"] #list of strings that contains names, with list we can store multiple values in a single variable
print(friends) #print the list
friends.pop() #remove the last item in the list
print(friends) #print the list

#check if an item is in the list using the index function, it will return the index of the item if it is in the list and it will return an error if the item is not in the list
print(friends.index("Kevin")) #print the index of Kevin in the list
#print(friends.index("Mike")) #print the index of oscar in the list

#to count the number of times an item appears in the list, we use the count function
print(friends.count("Jim")) #print the number of times Jim appears in the list

#another function is the sort function, it allows you to sort the items in the list in ascending order
friends.sort() #sort the items in the list in ascending order
print(friends) #print the list
lucky_numbers.sort() #sort the items in the list in ascending order
print(lucky_numbers) #print the list

#another function is the reverse function, it allows you to reverse the items in the list
lucky_numbers.reverse() #reverse the items in the list
print(lucky_numbers) #print the list

#another function is the copy function, it allows you to copy the items in the list to another list
friends2 = friends.copy() #copy the items in the list to another list
print(friends2) #print the list