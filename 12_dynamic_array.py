class DynamicArray:
    def __init__(self):
        self._data = [None]
        self._capacity = 1
        self._size = 0

    def __len__(self):
        return self._size

    def get(self, index):
        return self._data[index]

    def set(self, index, value):
        self._data[index] = value
        if index >= self._size:
            self._size = index + 1

    def pop(self):
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def append(self, element):
        if self._size == self._capacity:
            new_data = [None] * (self._capacity * 2)
            i = 0
            for elem in self._data: 
                new_data[i] = elem
                i+=1
            self._data = new_data
            self._capacity = self._capacity * 2
        self._data[self._size] = element
        self._size += 1

    def print_info(self):
        print(f"size: {self._size}, capacity: {self._capacity}")


Liste = DynamicArray()
for i in range(30):
    Liste.append(i)
    print(Liste._data)
    Liste.print_info()
print(Liste.get(5))
print(Liste._data)
Liste.set(5, "V")
print(Liste._data)
print(Liste.pop())
print(Liste._data)
Liste.print_info()
print(Liste.__len__())


