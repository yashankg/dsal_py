import array as hashTable
#Create an empty array of size 7 and Initialize all index to -1
size=7
hashTable = hashTable.array('i',[-1]*size)

def initial():
    print(hashTable) # Print empty hash table.

def insertHash(value): #this function is used to insert values into hash table
    key = value % size;
    if(hashTable[key] == -1):
        hashTable[key] = value;
        print(value,"inserted at arr",key);
    else:
        print("Collision : arr",key,"has element",hashTable[key],"already!");
        print("Unable to insert", value, "into hash table");

def search(value): #this function is used to search value into hash table
    key = value % size;
    if(hashTable[key]==value):
        print(value, "Found at", key,"th Index location");
    else:
        print(value, "Not Found at", key,"th Index location");
        
def delHash(value): #this function is used to delete value from hash table if present
    key = value % size;
    if(hashTable[key]==value):
        print(value, "Sussfully deleted from hash table");
        hashTable[key]=-1;
    else:
        print(value, "Not Found at", key,"th Index location");     

initial(); #Actual code starting to execute from this line.            
insertHash(7)
insertHash(0) #Showing Collision occure 
insertHash(13)
insertHash(10)
insertHash(4)
insertHash(15)
print(hashTable) # Print hash table along with data.

search(13) #searching operation in hash table
search(25)

delHash(13) #delete operation in hash table
print(hashTable) # Print hash table along with data.
