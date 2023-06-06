# Function to display hashtable
def display_hash(hashTable):

    for i in range(len(hashTable)):
        print(i, end = " ")
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
        print()

# Insert Function to add values to the hash table
def insert(Hashtable, keyvalue, value):
    keyvalue=keyvalue % len(HashTable)   # Hashing Function. 
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
# Creating Hashtable as a nested list.

# Driver Code
HashTable = [[] for i in range(8)] #Creating a nested list of size 10
insert(HashTable, 10, 'Allahabad')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 4, 'Mathura')
insert(HashTable, 9, 'Delhi')
insert(HashTable, 21, 'Punjab')
insert(HashTable, 31, 'Noida')

print(HashTable); # List representation to know how data stored in the list

display_hash (HashTable) #display function showing hashing operation with seprate chaining
