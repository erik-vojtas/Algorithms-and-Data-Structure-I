# Hash Table
# https://www.programiz.com/dsa/hash-table


class HashTable(object):
    def __init__(self, length=5): # initiate array with empty values.
        self.array = [None] * length


    def printHastTable(self): # print Hash Table
        returned_str = ""
        for item in self.array:
            if item is None:
                returned_str += "None, "
            else:
                for kvp in item:
                    returned_str += f"{kvp[0]}:{kvp[1]}, "
        print(returned_str)


    def getIndex(self, key): # get the index of array for a specific key
        length = len(self.array)
        return hash(key) % length


    def getValue(self, key): # get a value by key
        index = self.getIndex(key)
        if self.array[index] is None: # if key does not exist
            raise KeyError()
        else: # Loop through all key-value-pairs and find if key exist. If it does then return its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            raise KeyError() # of no return was done during loop, it means key didn't exist.


    def insertKVP(self, key, value): # insert key-value pair (KVP) to array by its key
        index = self.getIndex(key)
        if self.array[index] is not None: # this index already contain some values. This means that this add MIGHT be an update to a key that already exist. Instead of just storing the value we have to first look if the key exist.
            for kvp in self.array[index]: # if key is found, then update its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else: # if no breaks was hit in the for loop, it means that no existing key was found, so we can simply just add it to the end.
                self.array[index].append([key, value])
        else: # this index is empty. We should initiate a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])


    def removeKVP(self, key):
        index = self.getIndex(key)
        print(index)
        if self.array[index] is not None:  # this index already contain some values. This means that this add MIGHT be an update to a key that already exist. Instead of just storing the value we have to first look if the key exist.
            for kvp in self.array[index]:  # if key is found, then update its current value to the new value.
                if kvp[0] == key:
                    self.array.pop(index)
                    print("KVP has been deleted.")
                    break
                else:
                    print(f"Key: {key} has not been found.")
                    break
        else:
            print(f"Key: {key} has not been found.")


    def __repr__(self): # string representation of object
        returned_str = ""
        for item in self.array:
            if item is None:
                returned_str += "None, "
            else:
                for kvp in item:
                    returned_str += f"{kvp[0]}:{kvp[1]}, "
                    # print(kvp)
        return returned_str


ht = HashTable(5)
ht.printHastTable()

ht.insertKVP(1, "A")
ht.insertKVP(2, "B")
ht.insertKVP(3, "C")
ht.insertKVP(4, "D")
ht.insertKVP(5, "E")
ht.printHastTable()
print("-------------------------------------")
print(ht.getIndex("C"))
print(ht.getValue(2))
print("-------------------------------------")
ht.insertKVP(6, "F")
ht.printHastTable()
