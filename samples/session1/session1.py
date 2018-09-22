'''
Created on Sep 22, 2018

@author: nnhatkhanh
'''

#print("Hello")

friends = {
    "tom" : "098",
    "jerry" : "097"
    }

print("search:" + str("tom" in friends))

def my_function(a, b, c):
    return a + b + c

print("Result: " + str(my_function(1, 2, 3)))
print("Result: " + str(my_function(1, b=2, c=3)))
print("Result: " + str(my_function(1, c=2, b=3)))


