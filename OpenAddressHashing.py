class HashMap: #class of name hashmap or hashtable
        def __init__(self): #constructor is defined with 2 variables 
                self.size = 7  #setting an size of array as 6
                self.map = [None] * self.size #creating an empty array of size 6

        def _get_hash(self, key): #this function is used to get hash value of the key
                return key % self.size

        def add(self, key, value): #add take key and value 
                key_hash = self._get_hash(key)
                key_value = [key, value] #key value is constructing a list

                if self.map[key_hash] is None: 
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True

        def get(self, key): #get the hash values 
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None

        def delete(self, key): #delete an passed key from hashmap
                key_hash = self._get_hash(key)

                if self.map[key_hash] is None:
                        return False
                for i in range (0, len(self.map[key_hash])):
                        if self.map[key_hash][i][0] == key:
                                self.map[key_hash].pop(i)
                                return True
                return False

        def keys(self):
                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                arr.append(self.map[i][0])
                return arr

        def print(self):
                print('\n\n---PHONEBOOK----')
                for item in self.map:
                        if item is not None:
                                print(str(item))
                        else:
                                print("[NULL]");

h = HashMap()
h.add(7,'Kiran')
h.add(0,'Pooja')
h.add(9, 'Sandeep')
h.add(13,'Manisha')
h.add(10,'Ankit')
h.add(4,'Ram')
h.add(15,'Sonali')
h.print()
h.delete(9)
h.print()
print('\n\Pooja: ' + h.get(0))
print(h.keys())
