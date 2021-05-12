Challenge #3

We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.
Example Inputs object = {“a”:{“b”:{“c”:”d”}}}
				key = a/b/c 
				
			   object = {“x”:{“y”:{“z”:”a”}}}
    			key = x/y/z value = a
				
				
Solution:
In this solution we have a nested dictionary object {"a":{"b":{"c":"d"}}} and we are taking input from user for the key for this dictonary. 
User can Enter Key in the format,like "a or a/b or a/b/c".  Both of these object and key are passed to function getObjectKeys.
In this function we are splitting the keys passed in "/" format and in loop we are looking the keys and values in object items. It continues matching the keys of the items
with the one we provided, till it doesnot matches the key in the item. and provide that output.