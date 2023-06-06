import array as ar
#Array(data_type, value_list) is used to create an array with data type and value list specified in its arguments.
#i-Signed int, I-Unsigned int, l-Signed long, L-Unsigned long, f-Float, d-Double, c-Unicode
#[] is used to insert value in array from position 0
#len function is used to calculate total number of element in array
num = ar.array('i', [1, 2, 3])
ln=len(num)
print(ln) #length 

num[0] = 0  #changing first element  
print(num) 

num.append(4) #appending 4 to array
print(num)    

num.extend([5, 6, 7]) #extending numbers with 5,6,7
print(num) 
