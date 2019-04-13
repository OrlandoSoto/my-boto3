#!/usr/bin/python
import random

list_size = 10
my_list = []
 	
def func(list_to_sort):

    for num in range(1, len(my_list)):
      
      current_value = list_to_sort[num]

      while num > 0 and (list_to_sort[num] < list_to_sort[num -1]):

    	list_to_sort[num] = current_value
    	list_to_sort[num] = list_to_sort[num -1]
    	list_to_sort[num -1] = current_value
        num = num -1
        
    return list_to_sort

def test_answer():
    # Create an unsorted random list
    for num in range(list_size):
      my_number = random.randint(1,101)
      my_list.append(my_number)
    
    print "unsorted list"
    print my_list
    
    # Sort the list to use for test comparison
    sortedList = sorted(my_list)
    print "Sorted List:" 
    print sortedList
    
    returned_list = func(my_list)
    print "returned list"
    print returned_list

    assert sortedList == returned_list